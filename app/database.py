import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ 只在本機載入 `.env`
if os.getenv("RAILWAY_ENVIRONMENT_NAME") is None:
    load_dotenv()

# ✅ Railway 使用 `DATABASE_URL`，本機使用 `.env` 的 `DB_URL`
DB_URL = os.getenv("DATABASE_URL") if os.getenv("RAILWAY_ENVIRONMENT_NAME") else os.getenv("DB_URL")

# ✅ 確保 DB_URL 存在
if not DB_URL:
    raise ValueError("❌ DATABASE_URL or DB_URL is not set. Please check your environment variables.")

# ✅ Railway 需要 `sslmode=require`
if "sslmode" not in DB_URL and os.getenv("RAILWAY_ENVIRONMENT_NAME"):
    DB_URL += "?sslmode=require"

print(f"🚀 Connecting to database: {DB_URL}")  # ✅ Debug 訊息

# ✅ 建立 SQLAlchemy 引擎
engine = create_engine(DB_URL)

# ✅ ORM 基底類別
Base = declarative_base()

# ✅ Session 管理資料庫連線
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ **延遲導入，避免循環導入錯誤**
def init_db():
    """手動初始化資料庫表格（如果沒有 migration tool）"""
    from app.models import SummarizationHistory  # ✅ 避免 ImportError
    Base.metadata.create_all(bind=engine)

# ✅ Railway **自動執行 `init_db()`**，但在本機不會影響
if os.getenv("RAILWAY_ENVIRONMENT_NAME"):
    init_db()
