import asyncpg
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

# PostgreSQL connection details
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env file

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")


# Initialize FastAPI app
app = FastAPI()

async def create_table():
    pool = await asyncpg.create_pool(
        user=DB_USER, password=DB_PASS,
        database=DB_NAME, host=DB_HOST, port=DB_PORT
    )
    async with pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS documents (
                id SERIAL PRIMARY KEY,
                filename TEXT NOT NULL,
                content TEXT NOT NULL,
                embedding REAL[] NOT NULL,
                selected_for_qa BOOLEAN DEFAULT FALSE
            );
        """)
    await pool.close()

@app.on_event("startup")
async def startup_event():
    await create_table()





