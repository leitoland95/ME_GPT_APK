from pydantic import BaseModel
from typing import List, Dict, Any

class QueryRequest(BaseModel):
    text: str
    filenames: List[str] = []

class QueryResponse(BaseModel):
    result: str
    metadata: Dict[str, Any] = {}