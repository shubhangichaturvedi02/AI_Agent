
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from app.config import Config

import logging


SLACK_API_TOKEN = Config.SLACK_API_TOKEN
SLACK_CHANNEL =  Config.SLACK_CHANNEL

client = WebClient(token=SLACK_API_TOKEN)
logger = logging.getLogger(__name__)

def post_message(message: str):
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=message
        )
        print(response)
    except SlackApiError as e:
        logger.error(f"Error posting message to Slack: {e.response['error']}")

