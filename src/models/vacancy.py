from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship

from sqlalchemy import String, Text, DateTime, ForeignKey
from datetime import datetime
from typing import Optional

from src.database import Base
# from src.models.interview import Interview
# from src.models.users import UserModel


class Vacancy(Base):
    __tablename__ = "vacancies"

    vacancy_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    job_title: Mapped[str] = mapped_column(String(255), nullable=False)
    company_name: Mapped[str] = mapped_column(String(255), nullable=False)
    vacancy_text: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    level: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    source_link: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # user: Mapped["UserModel"] = relationship(back_populates="vacancies")
    # interviews: Mapped[list["Interview"]] = relationship(back_populates="vacancy")