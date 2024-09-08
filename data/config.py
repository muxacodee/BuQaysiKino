from dotenv import load_dotenv
import os

load_dotenv()

# Access the environment variables
API_TOKEN = os.getenv('API_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
