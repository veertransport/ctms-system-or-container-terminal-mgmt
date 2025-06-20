from pydantic import BaseModel
from typing import Optional

class Container(BaseModel):
    container_id: str
    type: str
    size: str
    line: str
    status: str  # e.g., "in-yard", "out-gate"

class User(BaseModel):
    username: str
    role: str  # e.g., "admin", "worker", "gate_op"
