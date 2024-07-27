from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello, World!"}


@app.get("/homework", status_code=HTTPStatus.OK, response_class=HTMLResponse)
def complete_homework():
    return """
    <hmtl>
    <title>Tarefa de Casa</title>
    <h1>Trabalho Feito</h1>
    </html>"""
