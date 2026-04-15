from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship

from sqlalchemy import String, Text, DateTime, ForeignKey
from datetime import datetime
from typing import Optional

from src.database import Base

class AnswerModel(Base):
    __tablename__ = "answers"

    answer_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    interview_id: Mapped[int] = mapped_column(ForeignKey("interviews.interview_id"), nullable=False)
    question_text: Mapped[str] = mapped_column(Text, nullable=False)
    answer_text: Mapped[str] = mapped_column(Text, nullable=False)
    answer_score: Mapped[int] = mapped_column(nullable=False, default=0)
    feedback_text: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)