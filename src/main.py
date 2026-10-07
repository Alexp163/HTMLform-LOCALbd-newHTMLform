from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Depends, Request, status


app = FastAPI()
templates = Jinja2Templates(directory="../templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/login", status_code=status.HTTP_200_OK)
async def login(request: Request):
    return templates.TemplateResponse(request=request, name="login.html" )


@app.get("/register", status_code=status.HTTP_201_CREATED)
async def register(request: Request):
    return templates.TemplateResponse(request=request, name="register.html")



