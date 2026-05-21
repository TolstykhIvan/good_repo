from flask import Flask, jsonify
import time

app = Flask(__name__)
time_requests_count = 0

@app.route('/time')
def get_time():
    global time_requests_count
    time_requests_count += 1
    return jsonify({"time": int(time.time())})

@app.route('/metrics')
def metrics():
    return jsonify({"count": time_requests_count})
