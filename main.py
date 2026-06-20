from supabase import create_client, Client
from dotenv import load_dotenv
import requests
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

dados = (
    supabase
    .table("contatos")
    .select("*")
    .limit(1)
    .execute()
)

if dados.data:

    contato = dados.data[0]

    nome = contato["nome"]
    telefone = contato["telefone"]

    mensagem = f"Olá, {nome} tudo bem com você?"

    url = (
        f"https://api.z-api.io/instances/"
        f"{os.getenv('ZAPI_INSTANCE_ID')}"
        f"/token/{os.getenv('ZAPI_TOKEN')}/send-text"
    )

    headers = {
        "Client-Token": os.getenv("ZAPI_CLIENT_TOKEN")
    }

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    resposta = requests.post(
        url,
        json=payload,
        headers=headers
    )

    print(resposta.text)