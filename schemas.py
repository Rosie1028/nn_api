from pydantic import BaseModel, Field, validator
from typing import Optional
from config import settings

class Article(BaseModel):
    """
    Schema for an article to be summarized.
    Attributes: text (str): The content of the article to summarize.
                        Must be between MIN_LENGTH and MAX_LENGTH characters.
    """
    text: str = Field(...,
                       min_length=settings.MIN_LENGTH,
                       max_length=settings.MAX_LENGTH,
                       description="The content of the article to summarize.",
                       example="This is an article about AI.")
    
    @validator('text')
    def validate_text(cls, v):
        if len(v) < settings.MIN_LENGTH:
            raise ValueError(f"Text must be at least {settings.MIN_LENGTH} characters long.")
        return v
