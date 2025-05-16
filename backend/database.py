import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def insert_agendamento(ag):
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(100),
            telefone VARCHAR(20),
            data DATE,
            horario TIME,
            servico VARCHAR(100)
        );
    """)
    cursor.execute("""
        INSERT INTO agendamentos (nome, email, telefone, data, horario, servico)
        VALUES (%s, %s, %s, %s, %s, %s);
    """, (ag.nome, ag.email, ag.telefone, ag.data, ag.horario, ag.servico))
    conn.commit()
    cursor.close()
    conn.close()

