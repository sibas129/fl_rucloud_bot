from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import MetaData, Sequence, UniqueConstraint, Column, Integer, BigInteger, String
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
    VarcharColumn
)


metadata_obj = MetaData(schema="public")


class Base(DeclarativeBase):
    metadata = metadata_obj


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[IntegerPrimaryKey] = mapped_column()
    telegram_id: Mapped[BigintColumn] = mapped_column(nullable=False)
    telegram_username: Mapped[VarcharColumn] = mapped_column(nullable=True)
    nextcloud_login: Mapped[VarcharColumn] = mapped_column(nullable=False, default="welcome")
    nextcloud_password: Mapped[VarcharColumn] = mapped_column(nullable=False, default="welcome")


class Groups(Base):
    __tablename__ = 'groups'

    id: Mapped[IntegerPrimaryKey] = mapped_column()
    telegram_id: Mapped[BigintColumn] = mapped_column(nullable=False)
    group_name: Mapped[VarcharColumn] = mapped_column(nullable=False)
    is_owner: Mapped[BoolColumn] = mapped_column(nullable=False, default=False)

