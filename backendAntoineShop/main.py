from fastapi import FastAPI
from routers.routes import router
from dependencies import *
from database import create_tables

app = FastAPI()
create_tables()

app.include_router(router)





