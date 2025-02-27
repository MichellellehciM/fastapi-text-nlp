from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse  
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import uvicorn
from app.routes import router  

app = FastAPI()

# 掛載 static 靜態文件
app.mount("/static", StaticFiles(directory="static"), name="static")
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
    port = int(os.getenv("PORT", 8000))  # 🔹 Railway 會自動提供 PORT
    uvicorn.run(app, host="0.0.0.0", port=port)
