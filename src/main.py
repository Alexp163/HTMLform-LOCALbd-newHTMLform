from fastapi import FastAPI

from view import router as view_router
from user_router import router 
from pacient_router import router2


app = FastAPI()
app.include_router(view_router)
app.include_router(router)
app.include_router(router2)
