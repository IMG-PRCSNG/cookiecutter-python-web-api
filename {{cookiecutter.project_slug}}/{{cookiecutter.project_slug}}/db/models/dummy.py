from typing import Optional
from sqlmodel import Field, SQLModel, create_engine


class Dummy(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
