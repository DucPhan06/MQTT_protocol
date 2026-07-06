# app.schemas.news.py

from pydantic import BaseModel

class NewsArticle(BaseModel):
    article_id: str
    title: str
    link: str
    source: str
    category: str
    duplicate: bool