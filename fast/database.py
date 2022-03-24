from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# try:
#     SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@{os.environ['POSTGRES_SERVER']}:{os.environ['POSTGRES_PORT']}/{os.environ['POSTGRES_DB']}"
# except KeyError:
#     from dotenv import dotenv_values
#     database_env = dotenv_values("database.env")
#     SQLALCHEMY_DATABASE_URL = f"postgresql://{database_env['POSTGRES_USER']}:{database_env['POSTGRES_PASSWORD']}@localhost:{database_env['POSTGRES_PORT']}/{database_env['POSTGRES_DB']}"
    
SQLALCHEMY_DATABASE_URL=os.environ('DATABASE_URL')

'''setup engine'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#eturns a class to create Base class => from this class to create each of the database models or classes
Base = declarative_base()


'''use to create independent db sessions for each request'''
def get_db():
    #instance of the SessionLocal class => the actual database session
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()