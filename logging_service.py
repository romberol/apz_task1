from flask import Flask, request, jsonify

app = Flask(__name__)
messages = {}


@app.route("/log", methods=["POST", "GET"])
def log():
    if request.method == "POST":
        data = request.json
        message_id = data['id']
        msg = data['msg']

        messages[message_id] = msg

        print(f"Received message: {msg} with ID: {message_id}")

        return jsonify({"status": "success"})
    elif request.method == "GET":
        all_messages = ", ".join(messages.values())
        return all_messages


if __name__ == '__main__':
    app.run(port=8081)
