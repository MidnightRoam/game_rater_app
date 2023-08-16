from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP

from src.database import Base


class Game(Base):
    """
    Represents a game entity in the database.

    Attributes:
        id (int): The unique identifier of the game.
        title (str): The title of the game, up to 255 characters in length.
        description (str): The description of the game.
        created_at (datetime): The timestamp indicating when the game record was created.

    Table Name:
        The table name in the database is 'game'.

    """
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True)
    title = Column(String(length=255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)




