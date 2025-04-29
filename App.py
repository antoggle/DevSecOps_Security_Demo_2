# app.py - Sample Vulnerable Python Web App (for DevSecOps Demo)
# modifying for PR 001

from flask import Flask, request
import os
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the DevSecOps Demo App"

@app.route('/greet')
def greet():
    user = request.args.get("user", "Guest")
    return f"Hello, {user}!"

@app.route('/search')
def search():
    query = request.args.get("q")
    conn = sqlite3.connect("demo.db")
    cursor = conn.cursor()
    # Intentional SQL injection vulnerability
    cursor.execute(f"SELECT * FROM users WHERE name = '{query}'")
    result = cursor.fetchall()
    conn.close()
    return str(result)

@app.route('/run')
def run():
    cmd = request.args.get("cmd")
    # Intentional command injection vulnerability
    output = os.popen(cmd).read()
    return output

if __name__ == "__main__":
    app.run(debug=True)
