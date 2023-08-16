from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import GameGet, GameCreate
from .service import _create_game
from src.database import get_db

router = APIRouter(prefix='/game', tags=['game'])


@router.post('/create', response_model=GameGet)
async def create_game(body: GameCreate, db: AsyncSession = Depends(get_db)):
    """
    Create a new game.

    Args:
        body (GameCreate): The data to create the new game.
        db (AsyncSession, optional): An asynchronous session to the database. Defaults to the dependency get_db.

    Returns:
        GameGet: The created game's data.
    """
    return await _create_game(body, db)
