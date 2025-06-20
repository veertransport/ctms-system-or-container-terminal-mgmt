from fastapi import APIRouter
from app.models import Container

router = APIRouter()

# In-memory container list (temporary placeholder)
containers_db = []

@router.post("/containers")
def create_container(container: Container):
    containers_db.append(container)
    return {"message": "Container added", "data": container}

@router.get("/containers")
def list_containers():
    return containers_db
