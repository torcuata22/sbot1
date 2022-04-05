import slackbot
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = slackbot.WebClient(token=os.environ['SLACK_TOKEN'])

