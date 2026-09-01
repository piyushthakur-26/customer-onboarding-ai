from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.database import Base


class OnboardingDecision(Base):
    __tablename__ = "onboarding_decisions"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True,
    )

    onboarding_case_id: Mapped[int] = mapped_column(
        ForeignKey("onboarding_cases.id"),
        nullable=False,
        unique=True,
        index=True,
    )

    decision: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    decided_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )