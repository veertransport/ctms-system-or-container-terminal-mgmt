from fastapi import FastAPI
import routes.containers as containers

app = FastAPI()

app.include_router(containers.router)

@app.get("/")
def read_root():
    return {"message": "CTMS backend is running"}
