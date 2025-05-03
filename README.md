# student_performance


```markdown
# 🎓 Student Performance Prediction Web App

This is a Flask-based web application that predicts student performance based on various factors like hours studied, previous scores, extracurricular activities, sleep hours, and practice habits. The app provides user authentication, prediction features, and stores results in a MongoDB database.

---

## 🔧 Features

- 🔐 User Registration and Login (JWT-based)
- 🔄 Forgot Password Functionality
- 📊 Predict Student Performance using trained ML model
- 💾 Store prediction results in MongoDB
- 🖼️ Responsive UI with background images and clean forms
- 🧠 Dynamic dropdown for Extracurricular Activities

---

## 🚀 Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB
- **Authentication**: Flask-JWT-Extended
- **Model**: Pretrained ML Model (`StudentPerformance` class)
- **Others**: Bootstrap styling (optional), AJAX via Fetch API

---

## 📁 Project Structure

```

project\_root/
│
├── app.py                     # Main Flask app with API routes
├── project\_app/
│   ├── database.py            # MongoDB connection functions
│   ├── utils.py               # ML model logic (StudentPerformance class)
├── project\_config.py          # App config (port, DB URI, etc.)
│
├── static/
│   ├── login.jpeg             # Background image for login
│   ├── forgot.jpeg            # Background image for forgot/register
│   ├── OIP.jpeg               # Background image for prediction
│
├── templates/
│   ├── login.html             # Login Page
│   ├── register.html          # Registration Page
│   ├── forgot.html            # Forgot Password Page
│   ├── prediction.html        # Main Prediction Page
│
└── README.md                  # You're here!

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/student-performance-app.git
cd student-performance-app
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> Make sure `Flask`, `flask-jwt-extended`, `pymongo`, etc., are included in `requirements.txt`.

### 4. Configure MongoDB

Update the `project_app/database.py` to include your MongoDB connection URI and create required collections:

* `user_collection`
* `testing_data_collection`

### 5. Run the App

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🌟 API Endpoints Overview

| Endpoint                              | Method | Description                       |
| ------------------------------------- | ------ | --------------------------------- |
| `/register`                           | POST   | Register a new user               |
| `/login`                              | POST   | Login and get JWT token           |
| `/forgot`                             | POST   | Reset password                    |
| `/prediction`                         | POST   | Predict performance (JWT token)   |
| `/Extracurricular_Activities_options` | GET    | Fetch dynamic dropdown data (JWT) |
| `/` or `/login.html`                  | GET    | Serve login HTML page             |

---

## 🔐 Authentication Flow

* After successful login, a JWT token is generated and stored in `localStorage`.
* This token is used in headers for making authenticated prediction requests.

---

## 📷 UI Screenshots

| Login                       | Register                        | Predict                     |
| --------------------------- | ------------------------------- | --------------------------- |
| ![login](static/login.jpeg) | ![register](static/forgot.jpeg) | ![predict](static/OIP.jpeg) |

---


