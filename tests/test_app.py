from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

client = TestClient(app)


def test_root_deve_retornar_ok_ola_mundo():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello, World!"}


def test_homework():
    client = TestClient(app)

    response = client.get("/homework")

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <hmtl>
    <title>Tarefa de Casa</title>
    <h1>Trabalho Feito</h1>
    </html>"""
    )
