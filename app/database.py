from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Code for connecting to database without sqlalchamy

# while True:
    
#     try:
#         conn = psycopg2.connect(host = 'localhost', database = 'fastapi', user = 'postgres',
#                              password = 'Klokje8520.', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was succesfull')
#         break
#     except Exception as error:
#         print("Connection to database failed")
#         print("Error:", error)
#         time.sleep(2)