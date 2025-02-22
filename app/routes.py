# routes.py - 負責處理 API 路由

from fastapi import APIRouter, Form, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.services import summarize_text
from app.database import SessionLocal
from app.models import SummarizationHistory
from sqlalchemy.orm import Session


# 初始化 API 路由
router = APIRouter()
templates = Jinja2Templates(directory="templates")

# 取得 DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 文章摘要 API
@router.post("/summarize", response_class=HTMLResponse)
def summarize_article(request: Request, text: str = Form(...), db: Session = Depends(get_db)):
    """ 處理表單輸入，回傳摘要與關鍵字 """
    summarized, keywords = summarize_text(text)
    history = SummarizationHistory(original_text=text, summarized_text=summarized, keywords=",".join(keywords))
    db.add(history)
    db.commit()
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "summary": summarized,
        "keywords": ", ".join(keywords)
    })
