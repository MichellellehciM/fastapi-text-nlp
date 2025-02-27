# routes.py - 負責處理 API 路由

from fastapi import APIRouter, Form, Depends
from fastapi.responses import JSONResponse
from app.services import summarize_text
from app.database import SessionLocal
from app.models import SummarizationHistory
from sqlalchemy.orm import Session

# 初始化 API 路由
router = APIRouter()

# 取得 DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 文章摘要 API (改為回傳 JSON)
@router.post("/summarize")
def summarize_article(text: str = Form(...), db: Session = Depends(get_db)):
    """處理表單輸入，回傳 JSON 格式的摘要與關鍵字"""
    summarized, keywords = summarize_text(text)
    
    # 儲存到資料庫
    history = SummarizationHistory(
        original_text=text, 
        summarized_text=summarized, 
        keywords=",".join(keywords)
    )
    db.add(history)
    db.commit()
    
    # 回傳 JSON
    return JSONResponse(content={
        "summary": summarized,
        "keywords": keywords
    })
