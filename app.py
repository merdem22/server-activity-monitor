from flask import Flask, jsonify
from metrics_collector import get_metrics

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def metrics():
    data = get_metrics()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)