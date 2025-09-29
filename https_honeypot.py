from flask import Flask, request, render_template_string, redirect
import logging
from datetime import datetime

app = Flask(__name__)

# Set up logging
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Secure Login</title>
</head>
<body>
    <h1>Secure Login</h1>
    <form method="POST" action="/login">
        <label>Username:</label>
        <input type="text" name="username"><br>
        <label>Password:</label>
        <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>
"""

@app.route('/')
def index():
    client_ip = request.remote_addr
    logging.info(f"HTTPS Request from {client_ip}: {request.method} {request.path}")
    return render_template_string(LOGIN_HTML)

@app.route('/login', methods=['POST'])
def login():
    client_ip = request.remote_addr
    username = request.form.get('username')
    password = request.form.get('password')
    logging.info(f"HTTPS Login Attempt from {client_ip}: Username: {username}, Password: {password}")
    return "Login successful! (Fake)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, ssl_context=('cert.pem', 'key.pem'), debug=False)
