from datetime import datetime

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, String, Integer, TIMESTAMP, Boolean, MetaData, Table, ForeignKey, Date, LargeBinary
from app.src.database import Base 



metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(320), unique=True, index=True, nullable=False),
    Column("username", String(100),unique=False, index=True),
    Column("hashed_password", String(), nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


profile = Table(
    "profile",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey(user.c.id)),
    Column("first_name", String(100),unique=False, index=True),
    Column("last_name",String(100),unique=False, index=True),
    Column("date_of_birth",Date),
    Column("photo",String(100),unique=False, index=True),

)

class User(SQLAlchemyBaseUserTable[int], Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    
    email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
    hashed_password: Mapped[str] = mapped_column(
            String(length=1024), nullable=False
        )
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
    is_verified: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User", backref='profile')
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    photo = Column(String)