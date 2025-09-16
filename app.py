# app.py
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calc', methods=['POST'])
def calc():
    data = request.get_json() or request.form
    try:
        a = float(data.get('a', ''))
        b = float(data.get('b', ''))
    except Exception:
        return jsonify({'error': 'Invalid numbers'}), 400

    op = data.get('op')
    if op == 'add':
        result = a + b
    elif op == 'sub':
        result = a - b
    elif op == 'mul':
        result = a * b
    elif op == 'div':
        if b == 0:
            return jsonify({'error': 'Division by zero'}), 400
        result = a / b
    else:
        return jsonify({'error': 'Invalid operation'}), 400

    return jsonify({'result': result})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
