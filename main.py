from numbers import Number
from typing import List
from fastapi import FastAPI, Response
from fastapi.responses import PlainTextResponse, HTMLResponse
from pydantic import BaseModel

app = FastAPI()
#PING fonctionnel
@app.get("/ping")
def ping():
    return {"message": "pong"}
#Q1
@app.get("/health")
def health():
    return Response(content="ok", media_type="text/plain", status_code=200)

phone_stocking = []
class Characteristic(BaseModel):
    ram_memory: Number
    rom_memory: Number

class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic
@app.post("/phones")

def phone(new_phones: List[Phone]):
    for phone in new_phones:
        phone_stocking.append(phone)
    return phone_stocking, Response(content="created", status_code=201)
@app.get("/phones")
def get_phones():
    return phone_stocking

@app.get("/phones/{id}")
def get_phone_by_id():
    return Phone