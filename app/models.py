from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from app.database import Base

class SummarizationHistory(Base):
    """ ORM 資料表模型，用來儲存使用者的摘要紀錄 """
    __tablename__ = "summarization_history"

    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(Text, nullable=False)  # 原始文本
    summarized_text = Column(Text, nullable=False)  # 產生的摘要
    keywords = Column(String, nullable=False)  # 關鍵字
    created_at = Column(DateTime, default=datetime.utcnow)  # 紀錄建立時間


