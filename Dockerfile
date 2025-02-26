# 1️⃣ 使用 Python 3.11 作為基礎映像（Slim 版本較輕量）
FROM python:3.11-slim

# 2️⃣ 設定工作目錄
WORKDIR /app

# 3️⃣ 安裝系統依賴（確保 PostgreSQL 連線不會出錯）
RUN apt-get update && apt-get install -y libpq-dev gcc

# 4️⃣ 複製需求文件並安裝 Python 依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ 複製專案文件
COPY . .

# 6️⃣ 設定 FastAPI 服務（限制 worker 避免 OOM）
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
