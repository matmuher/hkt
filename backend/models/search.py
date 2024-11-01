from pydantic import BaseModel
from typing import Optional


class Search(BaseModel):
    text: Optional[str]
    session_id: str
    filters: Optional[str]
