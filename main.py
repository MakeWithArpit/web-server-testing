from flask import Flask, request, jsonify

app = Flask(__name__)
latest_data = {}

@app.route('/data', methods=['POST'])
def receive_data():
    content = request.get_json()
    latest_data.update(content)
    return jsonify({"success": True})

@app.route('/')
def index():
    display = "<h1>Latest ESP32 Data</h1>"
    for k,v in latest_data.items():
        display += f"<p>{k}: {v}</p>"
    return display

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
