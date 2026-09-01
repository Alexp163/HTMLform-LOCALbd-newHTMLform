from fastapi import APIRouter, Request
from templates import render_template 

router = APIRouter(tags=["index"])

@router.get("/")
async def index(request: Request):
    return render_template("index.html", request=request)

