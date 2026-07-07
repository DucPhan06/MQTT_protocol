#app.repositories.article_repo.py

from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.article import Article
from app.schemas.news import NewsArticle


#save article if new, else skip
def save_article_if_new(db: Session, article_data: NewsArticle) -> bool:
    exist = db.scalars(select(Article).where(Article.article_id == article_data.article_id)).first()

    if(exist):
        return False
    
    article = Article(
        article_id=article_data.article_id,
        title=article_data.title,
        link=article_data.link,
        source_name=article_data.source_name,
        source_id=article_data.source_id,
        published_at=article_data.published_at,
    )

    db.add(article)
    db.commit()

    return True
