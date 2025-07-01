import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

if os.getenv("RAILWAY_ENVIRONMENT_NAME") is None:
    load_dotenv()

#  Railway 使用 `DATABASE_URL`，本機使用 `.env` 的 `DB_URL`
DB_URL = os.getenv("DATABASE_URL") if os.getenv("RAILWAY_ENVIRONMENT_NAME") else os.getenv("DB_URL")


if not DB_URL:
    raise ValueError("❌ DATABASE_URL or DB_URL is not set. Please check your environment variables.")

# 確保在連接到 PostgreSQL 時使用 SSL
if "sslmode" not in DB_URL and os.getenv("RAILWAY_ENVIRONMENT_NAME"):
    DB_URL += "?sslmode=require"

print(f" Connecting to database: {DB_URL}")  # Debug 訊息

# 建立 SQLAlchemy 引擎
engine = create_engine(DB_URL)

# 建立一個 ORM 的基底類別
Base = declarative_base() 

# Session 管理資料庫連線
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 資料庫初始化
def init_db():
    """手動初始化資料庫表格（如果沒有 migration tool）"""
    from app.models import SummarizationHistory  # ✅ 避免 ImportError
    Base.metadata.create_all(bind=engine)

# 如果在 Railway 環境中，則自動初始化資料庫
# 這樣可以確保在部署時資料庫表格已經存在
if os.getenv("RAILWAY_ENVIRONMENT_NAME"):
    init_db()
