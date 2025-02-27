import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 只在本機載入 .env，Railway 不會讀取
if os.getenv("RAILWAY_ENVIRONMENT_NAME") is None:
    load_dotenv()

# 🔹 優先使用 Railway 的 `DATABASE_URL`，如果沒有則使用本機 `DB_URL`
DB_URL = os.getenv("DATABASE_URL") if os.getenv("RAILWAY_ENVIRONMENT_NAME") else os.getenv("DB_URL")

# 🔹 確保 DB_URL 不是 None
if not DB_URL:
    raise ValueError("❌ DATABASE_URL or DB_URL is not set. Please check your environment variables.")

# 🔹 Railway 需要 `sslmode=require`
if "sslmode" not in DB_URL and os.getenv("RAILWAY_ENVIRONMENT_NAME"):
    DB_URL += "?sslmode=require"

# 建立 SQLAlchemy 資料庫引擎
engine = create_engine(DB_URL)

# 建立 ORM 的基底類別
Base = declarative_base()

# 建立 Session（管理資料庫連線）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
