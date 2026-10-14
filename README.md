# -IntroductionMCP

Exemplo introdutório de um servidor MCP em Python, usando transporte stdio.

## Requisitos

- Python 3.10 ou superior

## Instalação

```bash
python -m pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

O servidor disponibiliza a ferramenta `greet`, que recebe um nome e retorna
uma saudação. Como o transporte é stdio, execute-o por meio de um cliente MCP.
