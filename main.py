from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serve static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Simulated key store (replace with your bot's source)
valid_keys = {
    "ABC123": {"type": "perm"},
    "TEMP456": {"type": "temp", "expires_at": "2025-06-01T00:00:00Z"}
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/validate_key")
async def validate_key(key: str):
    key_info = valid_keys.get(key)
    if not key_info:
        return JSONResponse({"valid": False})

    # You could validate expiration here if it's a temp key
    return JSONResponse({"valid": True, "type": key_info["type"]})
