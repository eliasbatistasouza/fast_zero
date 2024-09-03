from http import HTTPStatus


def test_read_root(client):
    # client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello, World!'}  # Assert
