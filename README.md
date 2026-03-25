# My PWA Project

Proyecto de ejemplo que combina una API en FastAPI con una Progressive Web App (PWA) frontend.

## Estructura
- `backend` contiene la API en FastAPI.
- `static` contiene la PWA (HTML, CSS, JS, manifest, service worker, iconos).
- `tests` contiene pruebas con pytest.

## Desarrollo
1. Crear un entorno virtual e instalar dependencias:
   python -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt

2. Ejecutar la aplicación:
   uvicorn backend.main:app --reload --port 8000

3. Abrir http://localhost:8000

## Despliegue
- Se incluye un `Dockerfile` y `render.yaml` como ejemplo para desplegar en Render o en contenedores.