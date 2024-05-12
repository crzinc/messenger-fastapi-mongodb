# main.py

from fastapi import FastAPI
from routes.routes import user_router, chat_router, message_router

app = FastAPI()

app.include_router(user_router)
app.include_router(chat_router)
app.include_router(message_router)
