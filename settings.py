import os
import dotenv
dotenv.load_dotenv('.env')
TG_TOKEN_KEY=os.environ.get('TG_TOKEN_KEY')
CAT_API_KEY=os.environ.get('CAT_API_KEY')