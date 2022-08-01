from typing import List, Dict, Union

from fastapi import FastAPI, status, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory='app/templates')

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    data = {
            'page': 'Home Page'
    }
    return templates.TemplateResponse('home.html',
            {'request': request, 'data': data})
