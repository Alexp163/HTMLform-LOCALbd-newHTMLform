from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="../templates")


def render_template(request: Request, name: str, **kwargs):
    return templates.TemplateResponse(
        request=request,
        name=name,
        context=kwargs
        )



