import logging
from flask import Flask
from google.cloud import pubsub_v1

app = Flask(__name__)


@app.route("/", methods=["POST"])
def intake():
    try:
        report = requests.data
        publish_message(report)
        return 200
    except Exception as e:
        logging.error(e)
        return 500


def publish_message(report):
    publisher = pubsub_v1.PublisherClient()
    future = publisher.publish("projects/test-xcollantes/topics/reporting", report, spam="some spam value")
    logging.info(future.result())



if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0", debug=True)
