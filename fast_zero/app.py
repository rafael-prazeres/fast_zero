import asyncio
import sys
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.routers import auth, todos, users
from fast_zero.schemas import Message

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(todos.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {'message': 'Olá Mundo!'}


@app.get('/ola_mundo', status_code=HTTPStatus.OK, response_class=HTMLResponse)
async def read_root_html():
    return """
    <html>
        <head>
            <title>Nosso Olá Mundo!!!</title>
        </head>
        <body>
            <h1>Olá Mundo!</h1>
        </body>
    </html>"""
