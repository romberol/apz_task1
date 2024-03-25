from flask import Flask
from hazelcast_client import messages_queue
import sys
import threading

app = Flask(__name__)
messages_list = []


def consumer():
    print("Consumer started")
    while True:
        message = messages_queue.take()
        messages_list.append(message)
        print(f"Message received from queue: {message}")

threading.Thread(target=consumer, daemon=True).start()

@app.route('/messages', methods=['GET'])
def messages():
    static_message = " ".join(messages_list)
    return static_message


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("You need to specify port!!!")
        exit()

    app.run(port=int(sys.argv[1]))
