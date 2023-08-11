from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User
from .schemas import UserCreate, ShowUser
from  database import async_session


class UserDAL:
    """Data Access Layer for operating user info"""
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, username: str, email: str, hashed_password: str) -> User:
        new_user = User(
            username=username,
            email=email,
            hashed_password=hashed_password
        )
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user

    async def get_user(self, id: UUID) -> User:
        user_query = select(User).where(User.id == id)
        result = await self.db_session.execute(user_query)
        user = result.scalar()
        return user


async def _create_new_user(body: UserCreate, session) -> ShowUser:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.create_user(
            username=body.username,
            email=body.email,
            hashed_password=body.hashed_password
        )
        return ShowUser(
            id=user.id,
            username=user.username,
            email=user.email,
            name='',
            surname='',
            hashed_password=user.hashed_password,
            registered_at=user.registered_at,
            is_active=user.is_active,
            is_superuser=user.is_superuser,
            is_verified=user.is_verified,
        )


async def _get_user(user_id: UUID, session) -> ShowUser:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.get_user(id=user_id)
    return ShowUser(
        id=user.id,
        username=user.username,
        email=user.email,
        name='',
        surname='',
        hashed_password=user.hashed_password,
        registered_at=user.registered_at,
        is_active=user.is_active,
        is_superuser=user.is_superuser,
        is_verified=user.is_verified,
    )
