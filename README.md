# 🔐 Login System (Flask + MongoDB)

A simple and secure login & registration system built using Flask and MongoDB. This project demonstrates how authentication works in real-world applications with proper password hashing.

## 🚀 Features

* User Registration
* User Login Authentication
* Password Hashing using bcrypt
* MongoDB Integration (NoSQL)
* Error Handling for Invalid Credentials

## 🛠️ Tech Stack

* Python (Flask)
* MongoDB
* PyMongo
* bcrypt

## 📂 Project Structure

* app.py → Main backend logic
* templates/ → HTML files (login & register)

## 🔐 Security

Passwords are hashed using bcrypt before storing in the database, ensuring better security.

## ▶️ How to Run

1. Install dependencies:
   pip install flask pymongo bcrypt

2. Start MongoDB server

3. Run the app:
   python app.py

4. Open in browser:
   http://127.0.0.1:5000

## 📌 Future Improvements

* Session-based authentication
* UI improvements (Bootstrap)
* Input validation
* Role-based access (Admin/User)
