from engine import get_rag_chain
bot = get_rag_chain()
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class request_schema(BaseModel):
    question : str

@app.post("/ask")
async def Request(request:request_schema):
    response = bot.invoke(request.question)
    return {"answer":response}