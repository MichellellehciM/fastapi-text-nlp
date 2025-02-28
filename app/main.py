from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse  
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn
from app.routes import router  

app = FastAPI()

# 設定 CORS（確保 API 可以被前端存取）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 可更改成特定網域 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 掛載 static 靜態文件
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")), name="static")

# 掛載 templates 模板
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """ 顯示 HTML 頁面 """
    return templates.TemplateResponse("index.html", {"request": request})

# 掛載 API 路由
app.include_router(router)

# Railway 自動提供 PORT，確保相容性
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Railway 會自動提供 PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
