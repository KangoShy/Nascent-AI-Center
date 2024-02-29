# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from fastapi import FastAPI
from app.api import request_ai_control as rl

app = FastAPI()
# Register route to 'app'
app.include_router(rl.app, prefix="/chat")

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
