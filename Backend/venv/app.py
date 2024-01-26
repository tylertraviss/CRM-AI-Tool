from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['GET'])
def login():
    username = request.args.get('username', '')
    password = request.args.get('password', '')

    # Simple validation, you should implement secure authentication logic here
    if username == 'demo' and password == 'password':
        return jsonify({'message': f'Welcome, {username}!'})
    else:
        return jsonify({'message': 'Invalid credentials'})

if __name__ == '__main__': 
    app.run(debug=True)