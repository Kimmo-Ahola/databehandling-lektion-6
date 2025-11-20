from typing import Annotated, Optional
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, MetaData, String
from base import Base

str_255 = Annotated[str, mapped_column(String(255))]
int_pk = Annotated[int, mapped_column(Integer, primary_key=True, autoincrement=True)]

class Guest(Base):
    __tablename__ = "guests_table"
    # id INT PRIMARY KEY AUTO_INCREMENT
    id: Mapped[int_pk]
    first_name: Mapped[Optional[str_255]] # nullable
    last_name: Mapped[str_255] # not nullable
    email: Mapped[str_255] = mapped_column(unique=True)
    new_email: Mapped[str_255] = mapped_column(unique=True)