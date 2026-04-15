from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship

from sqlalchemy import String, Text, DateTime, ForeignKey
from datetime import datetime
from typing import Optional

from src.database import Base

class SkillModel(Base):
    __tablename__ = "skills"

    skill_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    skill_name: Mapped[str] = mapped_column(String(255), nullable=False)
    skill_category: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    skill_level: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    source_type: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)