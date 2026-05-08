from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship

from sqlalchemy import String, Text, DateTime, ForeignKey
from datetime import datetime


from typing import Optional

from src.database import Base
# from src.models.users import UserModel
# from src.models.vacancy import Vacancy


class Interview(Base):
    __tablename__ = "interviews"

    interview_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    vacancy_id: Mapped[Optional[int]] = mapped_column(ForeignKey("vacancies.vacancy_id"), nullable=True)
    interview_type: Mapped[str] = mapped_column(String(100), default="AI Interview")
    difficulty_level: Mapped[str] = mapped_column(String(100), default="medium")
    started_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    finished_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    score: Mapped[int] = mapped_column(default=0)
    interview_status: Mapped[str] = mapped_column(String(50), default="started")

    # user: Mapped["UserModel"] = relationship(back_populates="interviews")
    # vacancy: Mapped[Optional["Vacancy"]] = relationship(back_populates="interviews")