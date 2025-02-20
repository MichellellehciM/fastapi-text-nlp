import os
import psycopg2
from dotenv import load_dotenv

# 讀取 .env 檔案
load_dotenv()

# 取得環境變數
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")  
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# 建立連線
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("✅ 成功連線到 PostgreSQL！")
except Exception as e:
    print("❌ 連線失敗：", e)
