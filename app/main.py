from fastapi import FastAPI  
from fastapi.responses import JSONResponse  

# 初始化 FastAPI
app = FastAPI()


@app.get("/")
def home():
    """ 測試 API 是否正常運作 """
    return JSONResponse(content={"message": "Welcome to FastAPI NLP API!"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
