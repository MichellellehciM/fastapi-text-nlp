### **📖 專案簡介**
FastAPI 提供 API 和 前端頁面，使用 Jinja2 模板引擎 來渲染 HTML，
讓使用者可以輸入文本，並即時獲得 摘要與關鍵字。
### **📌 專案設計 (FastAPI + AI 應用)**

開發一個 FastAPI 應用，讓使用者輸入一段文章，系統會：

- 自動摘要（使用 NLP 演算法）
- 提取關鍵字（TF-IDF 或 spaCy）
- 儲存結果到資料庫（PostgreSQL）
- 提供 API 端點，讓前端或其他應用存取
- 架構：FastAPI（後端）+ AI（NLP）+ PostgreSQL（數據儲存）



---
### **📌 目標 :**
開發一個 **AI 驅動的 API**，提供：
1. **文本摘要**（LexRank）  
2. **關鍵字提取**（TF-IDF, TextRank）  
3. **支援中英文**（spaCy & 停用詞處理）  
4. **存取 PostgreSQL 資料庫**（儲存查詢記錄）  
5. **前端支援**（Jinja2 渲染 HTML）

**FastAPI 提供 API 和前端頁面**，使用者可在 **Web 介面輸入文本並獲得即時結果**

---

### **📌 技術 :**
1. **後端**：FastAPI  
2. **NLP**：spaCy, TF-IDF, TextRank  
3. **資料庫**：PostgreSQL, SQLAlchemy  
4. **前端模板**：Jinja2 + HTML/CSS  
5. **部署方式**
 - 本地開發：Uvicorn
 - 正式部署：(尚未)

---

## **🔧 安裝與使用**
### **1️⃣ 安裝環境**
```bash
git clone https://github.com/your-username/fastapi-text-nlp.git
cd fastapi-text-nlp
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
### **2️⃣ 設定 PostgreSQL**
```
CREATE DATABASE nlp;
```
### **3️⃣ .env 設定**
DATABASE_URL=postgresql://your_user:your_password@localhost/nlp

### **4️⃣ 啟動應用**
```
uvicorn app.main:app --reload
```
### **5️⃣ 打開瀏覽器**
http://127.0.0.1:8000

### **6️⃣ 輸入文章&生成摘要關鍵字**
 ![image](https://github.com/user-attachments/assets/d179af4e-9813-4a98-b9d0-afefce988acc)



## 介紹
本專案是一個基於 FastAPI 的 自然語言處理 (NLP) 應用，能夠自動從使用者文章中提取摘要與關鍵字，幫助使用者快速掌握內容重點。系統透過 API 接收使用者輸入的文本，分析後回傳 JSON 格式 的摘要與關鍵字，並以動態網頁方式呈現結果。

此專案使用 spaCy 和 jieba 進行中英文文本處理，並透過 LexRank 演算法選出重要句子作為摘要。同時，關鍵字提取部分結合 TextRank (中文) 和 TF-IDF (英文)確保準確度。此外，PostgreSQL 負責存儲摘要歷史，並透過 SQLAlchemy ORM 管理資料庫。

前端採用 HTML、CSS 和 JavaScript (Fetch API)，讓使用者輸入文本後，能夠即時獲取分析結果，而 Jinja2 則用於渲染模板。專案使用 Docker 進行容器化部署，確保環境一致性，並支援雲端部署。

