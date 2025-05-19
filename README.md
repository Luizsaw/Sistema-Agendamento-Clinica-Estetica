# 💆‍♀️ Sistema de Agendamento para Clínica de Estética

Este é um sistema simples e funcional para agendamento de horários em uma clínica de estética. Desenvolvido com foco em praticidade e automação, ele permite que clientes agendem serviços via interface web, enquanto a profissional recebe notificações por e-mail automaticamente.

---

### 🛠️ Arquitetura e Tecnologias

## 📚 Stack Tecnológica

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **Banco de Dados:** MySQL
- **Infraestrutura:** Docker e Docker Compose
- **Notificações:** Envio de e-mails via SMTP
- **Sistema Operacional:** Ubuntu Server (em máquina virtual)

---

## 📦 Estrutura do Projeto

```
📦 Sistema-Agendamento-Clinica-Estetica
├── 📂 backend
│   ├── 🐍 app.py               # Lógica principal da API
│   ├── 🗃️ database.py          # Conexão e operações com MySQL
│   ├── ✉️ email_utils.py       # Serviço de envio de e-mails
│   ├── 📜 requirements.txt     # Dependências Python
│   └── 🐳 Dockerfile           # Configuração da imagem Docker
├── 📂 frontend
│   ├── 🌐 index.html           # Interface de agendamento
│   ├── 🎨 style.css            # Estilos responsivos
│   └── 🛠️ script.js           # Lógica de interação
├── 🐳 docker-compose.yml       # Definição dos serviços
├── ⚙️ setup_clinica.sh         # Script de automação para Ubuntu
└── 🔒 .env.example             # Template de variáveis de ambiente
```

---

## 🚀 Implementação Rápida

### Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Ubuntu Server (pode rodar em VM)
- Acesso SMTP (ex: Gmail com senha de app)

---

### ⚡ Instalação em 3 Passos

#### 1. Clonar e configurar:
```bash
git clone https://github.com/seu-usuario/Sistema-Agendamento-Clinica-Estetica.git
cd Sistema-Agendamento-Clinica-Estetica
cp .env.example .env  # Configure com seus dados
```

#### 2. Inicializar com Docker:
```bash
docker-compose up --build -d
```

#### 3. Acessar o sistema:

---

## 🖥️ Frontend

- **URL de Acesso:** [`http://localhost:80`](http://localhost:80)

### ⚙️ Métodos de Execução

#### ✅ Método Recomendado (VS Code)

1. Instale a extensão **Live Server** no VS Code  
2. Clique com o botão direito no `index.html` e selecione **"Open with Live Server"**

#### 💻 Via Linha de Comando

```bash
cd frontend
python3 -m http.server 8080
```

- **Acesse em:** [`http://localhost:8080`](http://localhost:8080)

---

## 🔌 Backend (API)

- **URL Base:** [`http://localhost:5000`](http://localhost:5000)  
- **Documentação (Swagger UI):** [`http://localhost:5000/docs`](http://localhost:5000/docs)

---

## 🌐 Acesso via Máquina Virtual (VM)

### 🔍 Descobrir IP da VM (Ubuntu Server)

```bash
ip a
```

➡️ Procure um IP no formato `192.168.x.x`

### 🔗 Substituir `localhost` pelo IP da VM

- Exemplo de requisição:
```
http://192.168.56.101:5000/agendar
```

---

## ⚠️ Dicas Importantes

- 🔄 Verifique a **configuração de rede da VM** (modo Bridge ou NAT)
- 🔥 Confirme que o **firewall** permite conexões na porta `5000`
- 🌍 Para produção: utilize o **IP público** ou **domínio** do servidor

---

## 🖥️ Script de Automação para Ubuntu

- O script `setup_clinica.sh` pode ser utilizado para configurar rapidamente o ambiente em um servidor Ubuntu:

<details>
<summary>📜 Ver código do script</summary>

```bash
#!/bin/bash

echo "🚀 Configurando ambiente para a Clínica de Estética..."

# Atualização do sistema
echo "🔄 Atualizando pacotes..."
sudo apt update && sudo apt upgrade -y

# Instalação do Docker
echo "🐳 Instalando Docker..."
sudo apt install -y docker.io docker-compose
sudo systemctl enable docker
sudo usermod -aG docker $USER

# Estrutura do projeto
echo "📂 Criando estrutura de diretórios..."
mkdir -p /repo/Sistema-Agendamento-Clinica-Estetica/{frontend,backend}
cd /repo/Sistema-Agendamento-Clinica-Estetica

# Docker Compose
echo "📝 Gerando docker-compose.yml..."
cat <<EOF > docker-compose.yml
version: '3.8'

services:
  mysql:
    image: mysql:8.0
    container_name: mysql_clinica
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: rootpass
      MYSQL_DATABASE: agendamentos
      MYSQL_USER: user
      MYSQL_PASSWORD: userpass
    volumes:
      - mysql_data:/var/lib/mysql
    ports:
      - "3306:3306"

  backend:
    build: ./backend
    container_name: backend_clinica
    restart: always
    ports:
      - "5000:5000"
    depends_on:
      - mysql
    env_file:
      - .env

  frontend:
    image: nginx:alpine
    container_name: frontend_clinica
    volumes:
      - ./frontend:/usr/share/nginx/html:ro
    ports:
      - "80:80"

volumes:
  mysql_data:
EOF

# Configuração de ambiente
echo "🔧 Configurando variáveis..."
cat <<EOF > .env
DB_HOST=mysql
DB_USER=user
DB_PASSWORD=userpass
DB_NAME=agendamentos

EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha_app
EMAIL_PROFISSIONAL=profissional@clinica.com
EOF

# Backend setup
echo "🐍 Configurando backend..."
cat <<EOF > backend/requirements.txt
flask
mysql-connector-python
python-dotenv
pyjwt
EOF

cat <<EOF > backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
EOF

echo "✅ Configuração concluída com sucesso!"
echo "👉 Execute 'docker-compose up --build' para iniciar o sistema"
```

</details>

---

## 🔐 Segurança e Boas Práticas

> ⚠️ Não compartilhe o `.env` em repositórios públicos. Ele contém informações sensíveis como senhas de e-mail e credenciais do banco.

**Recomendações:**
- Utilize HTTPS com Let's Encrypt
- Implemente autenticação JWT para APIs
- Faça backups regulares do volume MySQL

---

## 📧 Configuração de E-mails

- Edite o `.env` com:
```ini
EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=sua_senha_app  # Use "Senha de App" do Google
EMAIL_PROFISSIONAL=recebedor@clinica.com
```

---

## 📌 Possíveis Melhorias Futuras

- Autenticação de usuários
- Painel administrativo para controle de agendamentos
- Confirmação de agendamento via e-mail
- Integração com WhatsApp

---

## 👨‍💻 Desenvolvedor

**Luiz Carlos de Araújo Machado**  
[LinkedIn](https://www.linkedin.com/in/luiz-machado-57366a174/)

---

## 🔐 Aviso Legal

> ⚠️ Este projeto é open-source sob licença MIT. Adapte as configurações de segurança para uso em produção.

- **Versão:** 1.0.0  
- **Última Atualização:** 19/05/2025
