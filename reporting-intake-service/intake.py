import logging
from flask import Flask, request
from google.cloud import pubsub_v1

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)


@app.route("/", methods=["POST"])
def intake():
    try:
        report = request.data
        j = request.get_json()
        publish_message(report)
        logging.info("Data from client: %s", j)
        return "Thanks, recievied message. " + str(j)
    except Exception as e:
        logging.error(e)
        return "ERROR"


def publish_message(report):
    publisher = pubsub_v1.PublisherClient()
    future = publisher.publish("projects/test-xcollantes/topics/reporting", report, spam="some spam value")
    logging.info(future.result())



if __name__ == "__main__":
    app.run(port=8080, host="0.0.0.0", debug=True)
