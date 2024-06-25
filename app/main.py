from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.database import engine, Base, get_db
from app.models import User
from app.schemas import UserCreate
from app.services import user_service

app = FastAPI()
templates = Jinja2Templates(directory="frontend/templates")

Base.metadata.create_all(bind=engine)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Home"})

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})

@app.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "title": "Register"})

@app.post("/register", response_class=HTMLResponse)
async def register_user(request: Request, db: Session = Depends(get_db), user_create: UserCreate = Depends()):
    try:
        user_service.create_user(db, user_create.username, user_create.email, user_create.password)
        return templates.TemplateResponse("login.html", {"request": request, "title": "Login"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(username="testuser").first()  # Replace with actual user fetching logic
    return templates.TemplateResponse("dashboard.html", {"request": request, "title": "Dashboard", "user": user})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)