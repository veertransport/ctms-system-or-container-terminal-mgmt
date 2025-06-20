from fastapi import FastAPI
from routes import containers

app = FastAPI()

app.include_router(containers.router)

@app.get("/")
def read_root():
    return {"message": "CTMS backend is running"}
