 # 開發過程記錄

## 2025-02-20 ~ 2025-02-21 環境設置
- 建立新 repository 名稱 fastapi-text-nlp
    - 初始化 README.md 和 .gitignore
    - git clone 到本地 
      cd fastapi-text-nlp
- 安裝 Microsoft C++ Build Tools   (Visual Studio Build Tools)
- 下載並安裝 Python 3.11 (spacy不支援 Python 3.13) 下載前要勾選 Add Python to PATH
- 建立開發環境
    - 虛擬環境 `py -3.11 -m venv .venv`
    - 啟用虛擬環境 `.venv/Scripts/activate`
    - 安裝相關套件 fastapi, uvicorn, sqlalchemy, psycopg2, pydantic, scikit-learn, spacy
    - 新增README.md
    - 新增requirements.txt
    - 下載 SpaCy 英文/中文語言模型 `python -m spacy download en_core_web_sm` `python -m spacy download en_core_web_sm`
- 設定 PostgreSQL
    - 登入 postgres
    - 建立新 database `create database nlp;`
    - 連到 nlp database `\c nlp`
    - 安裝 PostgreSQL 與 Python 的連接器 psycopg2-binary
- 建立 .env
    - 填入 PostgreSQL 的連線資訊
    - 安裝 python-dotenv (讀取 .env)
- 將預設分支從 main 改成 dev  (GitHub setting)
- 安裝 jinja2, fastapi, aiofiles

## 2025-02-21 Issue 1: 設置 FastAPI 環境
- 建立 main.py （FastAPI 入口）
    - (測試) API 啟動 FastAPI `uvicorn app.main:app --reload`
    - 點 http://127.0.0.1:8000 
    - NOTES: main.py 含以下功能
        1. 初始化 FastAPI 應用
        2. 掛載靜態文件（CSS、JS、圖片）
        3. 掛載 Jinja2 模板引擎（渲染 HTML 頁面）
        4. 定義首頁 / 的路由
        5. 載入 routes.py（API 路由）
        6. 啟動 FastAPI 伺服器

## 2025-02-22 Issue 2: 設置 FastAPI 環境
- 建立 database.py  (連線到 PostgreSQL 資料庫, 之後可將查詢結果存入 summarization_history 資料表)
    - 建立summarization_history table, 執行 `python -c "from app.database import Base, engine; import app.models; Base.metadata.create_all(bind=engine)"` 
- 建立 routes.py
    - NOTES: routes.py 含以下功能
        1. 定義 /summarize API 端點，讓使用者上傳文章，API 會回傳 摘要 & 關鍵字。
        2. 處理 HTML 表單的輸入（用 Form 取得 text）。
        3. 將摘要結果儲存到資料庫（PostgreSQL）。
        4. 使用 Jinja2 渲染 HTML 頁面，顯示摘要結果。
- 建立 services.py
    - NOTES: services.py 含以下功能
        1. 使用 NLP 模型（spaCy）分析輸入的文字，支援中英文
        2. 產生摘要（使用 LexRank 擷取最重要的句子，並動態調整摘要長度）
        3. 提取關鍵字（使用 TextRank 於中文，TF-IDF 於英文）
        4. 自動判斷輸入語言，確保適用對應的 NLP 模型
        5. 摘要輸出為條列式格式，提升可讀性
        6. 過濾停用詞（適用於中文 TextRank 提取關鍵字）

## 2025-02-24 完成前端頁面
- 建立 index.html（顯示輸入框與結果）
- 建立 style.css（美化前端介面）
- (測試) 
    1. API 啟動 FastAPI
    ```
    uvicorn app.main:app --reload
    ```
    2. 點進 http://127.0.0.1:8000
    3. 輸入 中文/英文 文章段落 會生成內容摘要和關鍵字 

## 2025-02-25 完成部署
- 安裝 Docker desktop 
- 建立 Dockerfile
- 建立 docker-compose.yml
- 建立 Docker image (會根據 Dockerfile 設定檔案執行)
    `docker build -t fastapi-text-nlp-json .`
- 運行 Docker container
    `docker run -p 8000:8000 fastapi-text-nlp-json`
- 使用 docker-compose 啟動服務
    `docker-compose up -d` (FastAPI 會自動連接 PostgreSQL，並且都會在 Docker 內運行)
- 本次嘗試兩種佈署方式: GitHub repo & image 上傳到 Docker Hub

## 套件與主要用途

| 套件                   | 主要用途                               |
|------------------------|----------------------------------|
| **FastAPI**            | 建立高效能的 API                  |
| **Uvicorn**            | 運行 FastAPI (ASGI 伺服器)        |
| **SQLAlchemy**         | 操作資料庫的 ORM                 |
| **psycopg2**           | PostgreSQL 的 Python 連接器      |
| **psycopg2-binary**    | PostgreSQL 連接器的二進位版本    |
| **Pydantic**           | 資料驗證與序列化                  |
| **Scikit-learn**       | 機器學習 (ML)                    |
| **spaCy**              | 自然語言處理 (NLP)               |
| **zh_core_web_sm**     | spaCy 的 **中文 NLP 模型**        |
| **en_core_web_sm**     | spaCy 的 **英文 NLP 模型**        |
| **spacy_pkuseg**       | spaCy 的 **中文斷詞模型**         |
| **Jinja2**             | 用於模板渲染 (HTML)              |
| **aiofiles**           | 非同步文件處理                   |
| **requests**           | 發送 HTTP 請求 (API 交互)        |
| **python-dotenv**      | 管理 `.env` 環境變數             |
| **networkx**           | 圖論分析，支援 TextRank & LexRank |
| **jieba**              | 中文分詞                          |
| **numpy**             | 數值計算                          |
| **scipy**             | 科學運算                          |
| **joblib**            | 機器學習模型存儲與載入           |
| **smart-open**        | 遠端讀取檔案 (支援 S3, GCS)      |
| **tqdm**              | 進度條顯示                        |
| **typer**             | 快速建立 CLI 指令行應用          |
| **Pygments**          | 程式碼高亮顯示                    |
| **rich**              | 終端輸出美化 (可顯示表格、顏色)  |
| **shellingham**       | 偵測終端環境 (CLI 自動補全)       |
| **MarkupSafe**        | Jinja2 安全處理 HTML 標籤        |
| **certifi**           | SSL 憑證驗證                      |
| **charset-normalizer** | 處理不同的字元編碼              |
| **urllib3**           | HTTP 請求處理                    |

---

### **套件組合的應用**
#### ** Web API 開發**
- **用 FastAPI 建 API**：開發高效能的 Web API 應用程式。
- **用 Uvicorn 來運行**：作為 ASGI 伺服器運行 FastAPI 應用。
- **用 SQLAlchemy + psycopg2 來存取 PostgreSQL**：ORM 模型操作資料庫。

#### ** 自然語言處理（NLP）**
- **用 spaCy 進行 NLP 分析**：詞性標註、命名實體辨識（NER）、依存關係分析。
- **用 `zh_core_web_sm` & `en_core_web_sm` 作為 NLP 模型**：支援中文 & 英文的文本處理。
- **用 `spacy_pkuseg` 提高中文分詞準確度**。
- **用 jieba 進行更靈活的中文分詞**。

#### ** 機器學習**
- **用 Scikit-learn 來訓練 ML 模型**：可用於分類、回歸、聚類等任務。
- **用 networkx 進行圖論分析**：支援 **TextRank（關鍵字提取）與 LexRank（文本摘要）**。
- **用 joblib 來存儲與載入模型**。

#### ** 其他輔助功能**
- **用 Jinja2 來渲染 HTML 頁面**：建立動態網頁，顯示結果或提供表單。
- **用 aiofiles 進行非同步文件處理**：提升檔案讀寫效能，例如處理上傳的文本檔案。
- **用 requests 發送 API 請求**：與外部 API 交互，獲取資料。
- **用 python-dotenv 管理環境變數**：避免將 API Key 直接寫在程式碼內。

---






手動啟動Fastapi
 `python -m uvicorn app.main:app --host 0.0.0.0 --port 8000`