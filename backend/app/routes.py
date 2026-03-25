from fastapi import APIRouter, UploadFile, File, Form
from typing import List, Optional
from .models import QueryRequest, QueryResponse
from .utils import process_query

router = APIRouter()

@router.post("/query", response_model=QueryResponse)
async def query_endpoint(
    text: Optional[str] = Form(None),
    files: Optional[List[UploadFile]] = File(None),
):
    """
    Recibe un texto y opcionalmente archivos, procesa la consulta y devuelve un resultado.
    El frontend envía el formulario multipart a /api/query.
    """
    filenames = [f.filename for f in files] if files else []
    req = QueryRequest(text=text or "", filenames=filenames)
    result = await process_query(req)
    return QueryResponse(result=result, metadata={"file_count": len(filenames)})