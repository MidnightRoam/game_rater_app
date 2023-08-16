from datetime import datetime

from pydantic import BaseModel


class GameCreate(BaseModel):
    """
    Alembic schema representing the data required to create a new game.

    Attributes:
        title (str): The title of the game.
        description (str): The description of the game.

    """
    title: str
    description: str


class GameGet(BaseModel):
    """
    Alembic schema representing the data structure of a game.

    Attributes:
        id (int): The unique identifier of the game.
        title (str): The title of the game.
        description (str): The description of the game.
        created_at (datetime): The timestamp indicating when the game record was created.

    """
    id: int
    title: str
    description: str
    created_at: datetime
