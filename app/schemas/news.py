# app.schemas.news.py

from pydantic import BaseModel, ConfigDict

class NewsArticle(BaseModel):
    model_config = ConfigDict(extra="forbid")

    article_id: str
    title: str
    link: str
    source_name: str
    source_id: str
    categories: list[str]
    language: list[str]
    country: list[str]
    #TODO: convert to datetime to store db
    published_at: str
    fetched_at: str
    #####
    duplicate: bool