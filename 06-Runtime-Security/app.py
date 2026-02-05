from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)

SECRET_KEY = "super-secret-password"

@app.route("/")
def home():
    return "Welcome to the Vulnerable App"

@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return str(result)

@app.route("/ping")
def ping():
    host = request.args.get("host")
    output = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return output

if __name__ == "__main__":
    app.run(debug=True)