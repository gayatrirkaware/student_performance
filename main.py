from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime
from project_app.database import get_db
from project_app.utils import StudentPerformance
import project_config
InsObj = StudentPerformance()

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'secret-key'
jwt = JWTManager(app)

user_collection,testing_data_collection = get_db()

######################################################################################

@app.route('/register', methods = ['POST'])
def register():
    user_data = request.form
    name = user_data.get('name','')
    username = user_data.get('username', '')
    password = user_data.get('password','')
    email_id = user_data.get('email_id','')
    mobile_number = user_data.get('mobile_number','')
    dob = user_data.get('dob','')

    response =  user_collection.find_one({'email_id':email_id})
    if not response:
        user_collection.insert_one({"name":name, 'username':username, 'password':password,
                    'email_id':email_id, 'mobile_number':mobile_number, 'dob':dob})
        return jsonify({"status": 'Success', "message" :  "User Registerd Successfully"})
    else:
        return jsonify({"status": 'Error', "message" :  "User already existy"})

@app.route('/login', methods = ['POST'])
def login():
    user_data = request.form
    username = user_data.get('username', '')
    password = user_data.get('password','')
    response =  user_collection.find_one({'username':username,'password':password})
    if response:
        access_token = create_access_token(identity = username, expires_delta= datetime.timedelta(minutes=5))
        print("access_token :",access_token)

        return jsonify({"status": 'Success', "message" :  "Login Successful", 
                        'token': access_token})
    else:
        return jsonify({"status": 'Error', "message" :  "Invalid Credentials"})

@app.route('/forgot', methods = ['POST'])
def forgot_password():
    user_data = request.form
    email_id = user_data.get('email_id', '')
    dob = user_data.get('dob','')
    new_password = user_data.get('new_password','')
    response =  user_collection.find_one({'email_id':email_id,'dob':dob})
    if response:
        user_collection.update_one({'email_id':email_id,'dob':dob}, 
                                   {"$set": {'password':new_password}})
        
        return jsonify({"status": 'Success', "message" :  "Password updated successfully"})
    
    else:
        return jsonify({"status": 'Error', "message" :  "User not exist"})

####################################################################################


@app.route("/")
def serve_login_page():
    return send_from_directory("templates", "login.html")



@app.route("/<path:filename>")
def serve_static_page(filename):
    return send_from_directory("templates", filename)

@app.route("/Extracurricular_Activities_options")
@jwt_required()
def extra_activities():
    col_data = InsObj.load_json_data()
    extra_activity_values = list(col_data['Extracurricular Activities'].keys())
    return jsonify(extra_activity_values)



@app.route("/prediction", methods = ["POST"])
@jwt_required()
def prediction():
    data = request.form
    
    predicted_performance = InsObj.predict_charges(data)

    print(f"Predicted Performance Index : {predicted_performance}")

    response = InsObj.save_data_in_db(testing_data_collection)
    if response:
        return jsonify({"result": f"Predicted Performance Index  : {predicted_performance}","message": "Result Successfully stored in Database"})
    else:
        return jsonify({"message": "Error"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=project_config.FLASK_PORT_NUMBER, debug=True)
