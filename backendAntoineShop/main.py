from fastapi import FastAPI
from routers.routes import router
from dependencies import *

app = FastAPI()



app.include_router(router)





