from flask import Flask, request, jsonify
import sys
from hazelcast_client import distributed_map

app = Flask(__name__)

@app.route("/log", methods=["POST", "GET"])
def log():
    if request.method == "POST":
        data = request.json
        message_id = data['id']
        msg = data['msg']

        distributed_map.put(message_id, msg)

        print(f"Received message: {msg} with ID: {message_id}")

        return jsonify({"status": "success"})
    elif request.method == "GET":
        all_messages = " ".join(list(distributed_map.values()))
        return all_messages


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("You need to specify port!!!")
        exit()

    app.run(port=int(sys.argv[1]))
