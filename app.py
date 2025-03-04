from flask import Flask, render_template, jsonify
from RetryPattern import fetch_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('visualizer.html')

@app.route('/fetch')
def get_data():
    try:
        data = fetch_data()
        return jsonify({'success': True, 'data': data})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)