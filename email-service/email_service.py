import logging
from flask import Flask, request

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def listen_for_pubsub():
    """Listen for PubSub reports."""
    try:
        report = request.data
        j = request.get_json()
        logging.info("Data from PubSub: %s", j)
        return "RECEIVED"
    except Exception as e:
        logging.error(e)
        return "ERROR"


if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0", debug=True)
