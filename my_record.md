 # 開發過程記錄

## 2025-02-20 環境設置
- 建立新 repository 名稱 fastapi-text-nlp
    - 初始化 README.md 和 .gitignore
    - git clone 到本地 
      cd fastapi-text-nlp
- 安裝 Microsoft C++ Build Tools   (Visual Studio Build Tools)
- 下載並安裝 Python 3.11 (spacy不支援 Python 3.13) 下載前要勾選 Add Python to PATH
- 建立開發環境
    - 虛擬環境 `py -3.11 -m venv .venv`
    - 啟用虛擬環境 `.venv/Scripts/activate`
    - 安裝相關套件 `pip install fastapi uvicorn sqlalchemy psycopg2 pydantic scikit-learn spacy`
    - 新增README.md
    - 新增requirements.txt
    - 下載 SpaCy 英文/中文語言模型 `python -m spacy download en_core_web_sm` `python -m spacy download en_core_web_sm`
- 設定 PostgreSQL
    - 登入 `psql -U postgres`
    - 建立新 database `create database nlp;`
    - 連到 nlp database `\c nlp`
    - 安裝 PostgreSQL 與 Python 的連接器 `pip install psycopg2-binary`
- 建立 .env
    - 填入 PostgreSQL 的連線資訊
    - 安裝 `pip install python-dotenv` (讀取 .env)

新增:
 FastAPI 同時提供 API 和 前端頁面，用 Jinja2 模板引擎 來渲染 HTML，讓使用者可以輸入文本，並即時獲得 摘要與關鍵字。


## 套件與主要用途

| 套件          | 主要用途                 |
|---------------|--------------------------|
| **FastAPI**   | 建立高效能的 API         |
| **Uvicorn**   | 運行 FastAPI (ASGI 伺服器) |
| **SQLAlchemy**| 操作資料庫的 ORM        |
| **psycopg2**  | PostgreSQL 的 Python 連接器 |
| **Pydantic**  | 資料驗證與序列化        |
| **Scikit-learn** | 機器學習 (ML)          |
| **spaCy**     | 自然語言處理 (NLP)     |

---

### 套件組合的應用
- **用 FastAPI 建 API**：開發高效能的 Web API 應用程式。
- **用 Uvicorn 來運行**：作為 ASGI 伺服器運行 FastAPI 應用。
- **用 SQLAlchemy + psycopg2 來存取 PostgreSQL 資料庫**：使用 ORM 模型與 PostgreSQL 資料庫進行操作。
- **用 Pydantic 來驗證 API 輸入**：確保請求的資料符合 API 規範。
- **用 Scikit-learn 來訓練機器學習模型**：實現分類、回歸或聚類等機器學習任務。
- **用 spaCy 來進行 NLP 分析**：進行詞性標註、實體辨識與文本解析等自然語言處理工作。

