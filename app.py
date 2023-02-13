from typing import Optional

from fastapi import FastAPI,Request
import uvicorn

from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from pydantic import BaseModel, Field
from uuid import UUID


app = FastAPI()

templates = Jinja2Templates(directory='templates')

app.mount(
    '/static',
    StaticFiles(directory=Path(__file__).parent.absolute()/'static'),
    name='static'
)

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


@app.get('/items/{item}')
async def get_item(item: str):
    return {'item name': item}


if __name__ == '__main__':
    uvicorn.run(app)


