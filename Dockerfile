# 1️⃣ 使用 Python 3.11 作為基礎映像
FROM python:3.11

# 2️⃣ 設定工作目錄
WORKDIR /app

# 3️⃣ 複製需求文件並安裝依賴
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4️⃣ 複製專案文件
COPY . .

# 5️⃣ 設定 FastAPI 服務
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]

# 避免佔用太多記憶體
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
