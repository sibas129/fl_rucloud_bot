from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, Sequence, UniqueConstraint
from datetime import datetime, timedelta
from db.orm.annotations import (
    IntegerPrimaryKey,
    BigintPrimaryKey,
    TextColumn,
    BoolColumn,
    BigintColumn,
    TimestampWTColumn,
    IntegerColumn,
    ListTextColumn,
)


metadata_obj = MetaData(schema="public")


class Base(DeclarativeBase):
    metadata = metadata_obj