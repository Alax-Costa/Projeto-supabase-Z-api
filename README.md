# Supabase + Z-API

Código em Python para ler pessoas cadastradas no Supabase e envie via Z-API

## Tabela do Supabase

campo                tipo

id                   bigint
nome                 text
telefone             text

Exemplo no Supabase

id                   nome             telefone
1                    Maria             21989542452


## Variáveis de ambiente

Crie um arquivo .env

SUPABASE_URL=https: colocar a url do supabase
SUPABASE_KEY= colocar a chave de acesso do supabase

ZAPI_INSTANCE_ID= colocar a id do Z-api
ZAPI_TOKEN= colocar o token
ZAPI_CLIENT_TOKEN= colocar o client token

## Instalação

pip install -r requirements.txt

## Execução

python main.py
