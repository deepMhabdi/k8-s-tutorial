from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

PORT = os.environ.get('PORT', 8000)

@app.route('/')
def home():


    return jsonify(message="Backend is running!")

@app.route('/ping')
def ping():
    return jsonify(message="Pong!")


if __name__ == '__main__':
    app.run(debug=True, port=PORT, host='0.0.0.0')

