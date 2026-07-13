from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

database_url="sqlite:///./sentinel.db"

engine=create_engine(database_url, connect_args={"check_same_thread": False})


SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)

base=declarative_base()