from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship

from sqlalchemy import String, Text, DateTime, ForeignKey
from datetime import datetime
from typing import Optional

from src.database import Base

class PreparationPlanModel(Base):
    __tablename__ = "preparation_plans"

    plan_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.user_id"), nullable=False)
    vacancy_id: Mapped[int] = mapped_column(ForeignKey("vacancies.vacancy_id"), nullable=False)
    weak_topics: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    recommended_topics: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    priority_level: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    generated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    plan_status: Mapped[str] = mapped_column(String(50), default="generated")