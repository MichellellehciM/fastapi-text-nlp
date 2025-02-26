# FastAPI 入口 - 只負責掛載路由，不處理 API 邏輯

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse  
from app.routes import router  # ✅ 掛載 routes.py
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os
import uvicorn


# 初始化 FastAPI
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    """ 顯示 HTML 頁面 """
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ 掛載 API 路由
app.include_router(router)

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    port = int(os.getenv("PORT", 8000))  # 🔹 Railway 會自動提供 PORT
    uvicorn.run(app, host="0.0.0.0", port=port)




