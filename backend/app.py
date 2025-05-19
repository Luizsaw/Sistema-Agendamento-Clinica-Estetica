from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import insert_agendamento
from email_utils import enviar_email
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #MV ip
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Agendamento(BaseModel):
    nome: str
    email: str
    telefone: str
    data: str
    horario: str
    servico: str

@app.post("/agendar")
def agendar(ag: Agendamento):
    try:
        insert_agendamento(ag)
        enviar_email(ag)
        return {"mensagem": "Agendamento realizado com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

