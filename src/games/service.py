from sqlalchemy.ext.asyncio import AsyncSession

from .models import Game
from .schemas import GameCreate, GameGet


class GameDAL:
    """
    Data Access Layer for operating game information.

    This class provides methods for interacting with game-related data in the database.

    Attributes:
        db_session (AsyncSession): An asynchronous session to the database.

    Methods:
        create_game: Creates a new game record in the database.

    """
    def __init__(self, db_session: AsyncSession):
        """
        Initialize the GameDAL with a database session.

        Args:
            db_session (AsyncSession): An asynchronous session to the database.
        """
        self.db_session = db_session

    async def create_game(self, title: str, description: str) -> Game:
        """
        Create a new game record in the database.

        Args:
            title (str): The title of the game.
            description (str): A detailed description of the game.

        Returns:
            Game: The created game object.

        """
        new_game = Game(
            title=title,
            description=description,
        )
        self.db_session.add(new_game)
        await self.db_session.flush()
        return new_game


async def _create_game(body: GameCreate, session) -> GameGet:
    """
    Create a new game record in the database and return its details.

    Args:
        body (GameCreate): The data containing the title and description of the game.
        session (AsyncSession): An asynchronous session to the database.

    Returns:
        GameGet: The details of the created game, including its id, title, description,
                 and creation timestamp.

    """
    async with session.begin():
        game_dal = GameDAL(session)
        game = await game_dal.create_game(
            title=body.title,
            description=body.description
        )
        return GameGet(
            id=game.id,
            title=game.title,
            description=game.description,
            created_at=game.created_at,
        )
