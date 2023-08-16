from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ShowUser, UserCreate
from .service import _create_new_user, _get_user, _get_users
from src.database import get_db

router = APIRouter(prefix='/user', tags=['user'])


@router.post("/create", response_model=ShowUser)
async def create_user(body: UserCreate, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _create_new_user(body, db)


@router.get('/users', response_model=List[ShowUser])
async def get_users(db: AsyncSession = Depends(get_db)) -> List[ShowUser]:
    return await _get_users(db)


@router.get('/{user_uuid}', response_model=ShowUser)
async def get_user(user_uuid: UUID, db: AsyncSession = Depends(get_db)) -> ShowUser:
    return await _get_user(user_uuid, db)