from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
student_api_url = os.getenv('STUDENT_API_URL')
