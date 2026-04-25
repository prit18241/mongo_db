from flask import Flask, render_template,request
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db = client['user_db']
users   = db['users']

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
   if request.method == "POST":
       username = request.form["username"]
       password = request.form["password"].encode('utf-8')
       user = users.find_one({"username": username})
       if user and bcrypt.checkpw(password, user["password"]):
           return "Login successful!"
       else:
           return render_template("login.html", error="Invalid username or password.   Try again.")
   return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password").encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        users.insert_one({"username": username, "password": hashed})
    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)