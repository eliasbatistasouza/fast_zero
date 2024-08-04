from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(
        username='elias', email='elias@email.com', password='minhasenha'
    )
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'elias'))

    assert user.username == 'elias'
