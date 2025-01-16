import abc
import time
from dataclasses import dataclass

# import pika
# import requests

AMQP_URL = ""
MODEL_VERSION_ID = "model_version_id"
SLEEP_DURATION = 60


# Data
@dataclass(frozen=True, kw_only=True)
class ALCCredentials:
    # https://anylogic.help/cloud/api/rest.html#endpoints
    endpoint: str = (
        f"https://cloud.anylogic.com/api/open/8.5.0/versions/{MODEL_VERSION_ID}/run"
    )
    api_key: str


# https://anylogic.help/cloud/api/rest.html#run-request-object
@dataclass(frozen=True, kw_only=True)
class Inputs:
    # This could contain the actual data from the queue
    # negatting the need for RMQ logic in the model.
    RabbitMQConnection: str
    queueName: str


@dataclass(frozen=True, kw_only=True)
class RequestData:
    experimentName: str
    inputs: Inputs


# Interface
class Broker(abc.ABC):
    @abc.abstractmethod
    def has_new_message(self, channel_name: str) -> bool:
        """Check whether given channel has a new message."""


class ALModel(abc.ABC):
    @abc.abstractmethod
    def awaken(self, alc_credentials: ALCCredentials, request_data: RequestData):
        """Make post request to Anylogic Cloud."""


# Application


class Wabbit:
    @staticmethod
    def run():
        while True:
            _ = 1 + 1
            time.sleep(SLEEP_DURATION)


if __name__ == "__main__":
    Wabbit.run()


# TO-DO
# - A way to recognize only wake up the model if a message is new.
