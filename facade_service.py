from flask import Flask, request
import requests
import uuid
import random

app = Flask(__name__)
logging_services_url = ["http://localhost:8082", "http://localhost:8083", "http://localhost:8084"]
messages_service_url = "http://localhost:8081"


@app.route("/facade_service", methods=["POST", "GET"])
def facade_service():
    if request.method == "POST":
        msg = request.data.decode("utf-8")
        message_id = str(uuid.uuid4())

        logging_service_url = random.choice(logging_services_url)
        requests.post(f"{logging_service_url}/log", json={'id': message_id, 'msg': msg})

        return ''
    elif request.method == "GET":
        logging_service_url = random.choice(logging_services_url)
        logging_response = requests.get(f"{logging_service_url}/log")
        messages_response = requests.get(f"{messages_service_url}/messages")

        combined_message = f"[{logging_response.text}] : {messages_response.text}"

        return combined_message


if __name__ == '__main__':
    app.run(port=8080)
