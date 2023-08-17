from typing import List, Dict
from uuid import UUID

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User
from .schemas import UserCreate, ShowUser
from  src.database import async_session


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

    async def get_user(self, user_id: UUID) -> User:
        user_query = select(User).where(User.id == user_id)
        result = await self.db_session.execute(user_query)
        user = result.scalar()
        return user

    async def get_users(self) -> List[User]:
        user_query = select(User).where(User.is_active == True)
        result = await self.db_session.execute(user_query)
        users = result.scalars().all()
        return users

    async def delete_user(self, user_id: UUID) -> User:
        user_query = update(User).where(User.id == user_id).values(is_active=False)
        await self.db_session.execute(user_query)
        await self.db_session.commit()


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
        user = await user_dal.get_user(user_id=user_id)
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


async def _get_users(session) -> List[ShowUser]:
    async with session.begin():
        user_dal = UserDAL(session)
        users = await user_dal.get_users()

        user_list = []
        for user in users:
            user_data = ShowUser(
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
            user_list.append(user_data)
        return user_list


async def _delete_user(user_id, session) -> ShowUser:
    async with session.begin():
        user_dal = UserDAL(session)
        user = await user_dal.delete_user(user_id)
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
