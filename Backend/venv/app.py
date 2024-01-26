from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Dictionary to store usernames and passwords (plaintext for demonstration)
users = {'admin': 'password'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['GET'])
def login():
    username = request.args.get('username', '')
    password = request.args.get('password', '')

    # Check if the username exists
    if username in users and users[username] == password:
        return jsonify({'message': f'Welcome, {username}!'})
    else:
        return jsonify({'message': 'Invalid credentials'})

if __name__ == '__main__':
    app.run(debug=True)
