import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def enviar_email(ag):
    msg = EmailMessage()
    msg['Subject'] = "Novo Agendamento Recebido"
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = os.getenv("EMAIL_PROFISSIONAL")

    msg.set_content(f"""
Novo agendamento:

Nome: {ag.nome}
Email: {ag.email}
Telefone: {ag.telefone}
Data: {ag.data}
Horário: {ag.horario}
Serviço: {ag.servico}
    """)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)

