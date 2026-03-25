from .models import QueryRequest
import asyncio

async def process_query(req: QueryRequest) -> str:
    """
    Lógica simple de ejemplo que combina el texto con los nombres de archivos.
    En un proyecto real aquí se integraría con modelos, búsquedas, etc.
    """
    # Simular trabajo asíncrono
    await asyncio.sleep(0.05)
    parts = []
    if req.text:
        parts.append(f"Texto recibido: {req.text}")
    if req.filenames:
        parts.append(f"Archivos recibidos: {', '.join(req.filenames)}")
    if not parts:
        return "No se recibió texto ni archivos."
    return " | ".join(parts)