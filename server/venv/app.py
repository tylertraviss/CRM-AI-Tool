from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dictionary to store user information
user_info = {'name': 'John Doe'}  # Default name for demonstration purposes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/userinfo', methods=['GET'])
def get_user_info():
    return jsonify({**user_info})

@app.route('/api/setoption', methods=['POST'])
def set_option():
    data = request.json
    selected_option = data.get('selectedOption', '')
    # Process the selected option as needed
    # For now, just update the user_info dictionary with the selected option
    user_info['selectedOption'] = selected_option
    return jsonify({'message': f'Selected option set to: {selected_option}'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
