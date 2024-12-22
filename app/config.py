import os 
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = f"mysql://{os.getenv('USER')}:{os.getenv('PSWD')}@{os.getenv('HOST')}:{os.getenv('PORT')}/{os.getenv('DB')}"