# Projeto Fila - 4º Semestre

Este projeto faz parte do 4º semestre do curso de Análise e Desenvolvimento de Sistemas da Toledo Presidente Prudente, na disciplina de **Desenvolvimento de APIs e Microsserviços**.

## Professor

**Prof. Me. Eli Candido Junior**

## Descrição

O objetivo deste projeto é desenvolver um backend em python responsavel por gerenciar uma fila.

## Estrutura do Projeto

```bash
4semestre_DesenvApiMicroServicos/
│
├── integracao.py      # Arquivo principal
├── db.json            # Arquivo do TinyDB
├── controllers/       # Diretório dos controllers da API
├── database/          # Diretório orquestrador do db
├── domain/            # Diretório responsavel pelos objetos do sistema
├── models/            # Diretório responsavel pelos modelos da base de dados
└── utils/             # Diretório responsavel pelos arquivos uteis para os sistemas
```

## Configuração e Execução

```bash
    #Ambiente Windows
Criação
    ├── uvicorn integracao:app --reload
URL
    http://127.0.0.1:8000
Swagger
    ├── http://127.0.0.1:8000/docs
```

## Requisitos

```bash
├── Python 3.7+
├── Uvicorn
```
