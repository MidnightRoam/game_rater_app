from datetime import datetime
import uuid

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import UUID, Column, String, TIMESTAMP, Boolean

from database import Base


class User(SQLAlchemyBaseUserTable[UUID], Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    email = Column(String, nullable=True, unique=True)
    hashed_password = Column(String(length=124), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
