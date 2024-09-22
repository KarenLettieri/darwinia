import asyncpg
import os

# Create a connection pool to the database
async def create_db_pool():
    return await asyncpg.create_pool(
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "root"),
        database=os.getenv("DB_NAME", "expenses_db"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )
