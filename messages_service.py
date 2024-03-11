from flask import Flask

app = Flask(__name__)


@app.route('/messages', methods=['GET'])
def messages():
    static_message = "not implemented message from messages-service"
    return static_message


if __name__ == '__main__':
    app.run(port=8081)
