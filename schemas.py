from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    new: str
    #url: Optional[str] = None