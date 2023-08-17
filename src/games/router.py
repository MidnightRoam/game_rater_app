from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import GameGet, GameCreate
from .service import _create_game, _get_game, _get_games, _delete_game
from src.database import get_db

router = APIRouter(prefix='/games', tags=['games'])


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


@router.get('/all', response_model=List[GameGet])
async def get_games(db: AsyncSession = Depends(get_db)) -> List[GameGet]:
    return await _get_games(db)


@router.get('/{game_id}', response_model=GameGet)
async def get_game(game_id: int, db: AsyncSession = Depends(get_db)) -> GameGet:
    return await _get_game(game_id, db)


@router.delete('/delete/{game_id}', response_model=dict)
async def delete_game(game_id: int, db: AsyncSession = Depends(get_db)) -> GameGet:
    return await _delete_game(game_id, db)
