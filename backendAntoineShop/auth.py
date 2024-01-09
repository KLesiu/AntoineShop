from datetime import timedelta,datetime
from jose import JWTError,jwt
import os
from dotenv import load_dotenv

load_dotenv()

def create_access_token(username:str,user_id):
    encode = {'sub':username,'id':user_id}
    expires_delta= timedelta(minutes=60)
    expires = datetime.utcnow()+expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,os.getenv("SECRET_KEY"),algorithm=os.getenv("ALGORITHM"))
    