from http import HTTPStatus


def test_creat_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'testusername',
            'email': 'test@email.com',
            'password': 'testpassword',
        },
    )

    # Validar UserPublic
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'testusername',
        'email': 'test@email.com',
    }
