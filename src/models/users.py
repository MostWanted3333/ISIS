from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship

from sqlalchemy import String, Text, DateTime, ForeignKey
from datetime import datetime
from typing import Optional

from src.database import Base

class UserModel(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(100), default="candidate")
    target_position: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    account_status: Mapped[str] = mapped_column(String(50), default="active")

    # resumes: Mapped[list["Resume"]] = relationship(back_populates="user")
    # vacancies: Mapped[list["Vacancy"]] = relationship(back_populates="user")
    # interviews: Mapped[list["Interview"]] = relationship(back_populates="user")  