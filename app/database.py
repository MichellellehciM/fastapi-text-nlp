import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base ,sessionmaker

load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")  # Railway的變數

# 當沒有 DATABASE_URL 變數時，使用本地端的 PostgreSQL 連線資訊
if not DATABASE_URL:
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD") 
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_URL = os.getenv("DB_URL")

# PostgreSQL 連線字串
# DB_URL = os.getenv("DB_URL")  


# 建立 SQLAlchemy 資料庫引擎
engine = create_engine(DB_URL)

# 建 ORM clasee 的基底類別
Base = declarative_base()

# 建資料庫 Session（管理資料庫連線）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



