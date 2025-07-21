from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from llm_interface import get_sql_query, format_answer

app = FastAPI()


class Question(BaseModel):
    query: str

@app.post("/ask")
async def ask_question(q: Question):
    
    sql = get_sql_query(q.query)

    try:
        
        conn = sqlite3.connect("ecommerce.db")
        cursor = conn.cursor()

        
        result = cursor.execute(sql).fetchall()

        conn.close()
    except Exception as e:
        result = f"❌ Error: {e}"

    
    return format_answer(q.query, sql, result)
