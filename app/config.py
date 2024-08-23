import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")
    SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "#code")
    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")
