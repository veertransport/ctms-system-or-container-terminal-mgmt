from fastapi import FastAPI
from app.routes import containers

app = FastAPI()

# Register container routes
app.include_router(containers.router)

@app.get("/")
def read_root():
    return {"message": "CTMS backend is running"}
