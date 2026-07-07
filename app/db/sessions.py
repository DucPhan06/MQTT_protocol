#app.db.sessions.py

#python connect to postgre

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.psql_config import DATABASE_URL

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)