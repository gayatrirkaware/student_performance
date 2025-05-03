import project_config
import pandas as pd
import numpy as np

import pickle
import json


class StudentPerformance():
    def __init__(self):
        pass

    def load_model(self):
        """
            This method will be used to loading Linear Regression Model
        """
        with open(project_config.MODEL_FILE_PATH, "rb") as f:
            self.linear_regression_model = pickle.load(f)
        
        self.feature_names = self.linear_regression_model.feature_names_in_
        return self.feature_names
    
    def load_json_data(self):
        """
            This method will be used to Load data from JSON files
            Data:
                Label Encoding Data
                OneHot Encoding Data
        """
        with open(project_config.LABEL_ENC_DATA_PATH, "r") as f:
            self.column_encoded_data = json.load(f)
        return self.column_encoded_data

    def get_data_from_user(self):
        self.load_model()
        self.load_json_data()
        Hours_Studied = eval(self.data['Hours Studied'])
        Previous_Scores = eval(self.data['Previous Scores'])
        Extracurricular_Activities = self.data['Extracurricular Activities']
        Sleep_Hours = eval(self.data['Sleep Hours'])
        Sample_Question_Papers_Practiced = self.data['Sample Question Papers Practiced']


        test_array = np.zeros((1,self.feature_names.size))
        test_array[0,0] = Hours_Studied
        test_array[0,1] = Previous_Scores
        test_array[0,2] = self.column_encoded_data['Extracurricular Activities'][Extracurricular_Activities]
        test_array[0,3] = Sleep_Hours
        test_array[0,4] = Sample_Question_Papers_Practiced
        self.df_test = pd.DataFrame(test_array, columns= self.feature_names)
        print(self.df_test)


    def predict_charges(self, data):
        self.data = data
        self.get_data_from_user()
        self.prediction = self.linear_regression_model.predict(self.df_test)[0]
        print('Predicted Price is:',np.around(self.prediction,3))
        return self.prediction
    
    def save_data_in_db(self, testing_data_collection):

        input_data = dict(self.data)
        input_data.update({'Prediction':self.prediction})
        testing_data_collection.insert_one(input_data)
        return "Sucessful"






    




