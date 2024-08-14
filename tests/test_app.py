from http import HTTPStatus

from fast_zero.schemas import UserPublic


def test_read_root(client):
    # client = TestClient(app)  # Arrange

    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Hello, World!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'elias',
            'email': 'elias@email.com',
            'password': 'minhasenha',
        },
    )

    # Validar UserPublic
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'elias',
        'email': 'elias@email.com',
    }


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}


def test_read_users_when_populated(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': [user_schema]}


def test_read_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'elias',
        'email': 'elias@email.com',
        'id': 1,
    }


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'giselle',
            'email': 'giselle@email.com',
            'password': 'outrasenha',
        },
    )
    # Testar status code 404
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'giselle',
        'email': 'giselle@email.com',
        'id': 1,
    }


def test_update_user_not_found(client, user):
    response = client.put(
        '/users/2',
        json={
            'username': 'giselle',
            'email': 'giselle@email.com',
            'password': 'outrasenha',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client, user):
    response = client.delete('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_read_user_not_found(client, user):
    response = client.get('/users/2')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
