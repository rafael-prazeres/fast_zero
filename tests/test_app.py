from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_root_deve_retornar_ok_e_ola_mundo_html(client):
    response = client.get('/ola_mundo')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>Olá Mundo!</h1>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'rafael.prazeres',
            'email': 'rafael.prazeres@ufrn.br',
            'password': '123456',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'rafael.prazeres',
        'email': 'rafael.prazeres@ufrn.br',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'rafael.prazeres',
                'email': 'rafael.prazeres@ufrn.br',
                'id': 1,
            }
        ]
    }


def test_read_user(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'rafael.prazeres',
        'email': 'rafael.prazeres@ufrn.br',
        'id': 1
    }


def test_read_user_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'user',
            'email': 'user@example.com',
            'password': '654321',
        }
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'user',
        'email': 'user@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'user',
            'email': 'user@example.com',
            'password': '654321',
        }
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {
        'detail': 'User not found',
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_user_not_found(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
