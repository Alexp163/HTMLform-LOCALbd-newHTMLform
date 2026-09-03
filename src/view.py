from fastapi import APIRouter, Request
from src.template import render_template 

router = APIRouter(tags=["index"])

@router.get("/")
async def index(request: Request):
    print("залупа")
    return render_template("index.html", request=request)


