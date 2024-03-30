# Bem vindo!

# Índice
* [Apresentação do Projeto](#Apresentação-do-Projeto)
* [Ferramentas do Projeto](#Ferramentas-do-Projeto)
* [Configuração Inicial](#Configuração-Inicial)

# Apresentação do Projeto
Este projeto é desenvolvido por estudantes da UNIVESP. Tem como objetivo auxiliar professores a aplicar em sala de aula atividades em grupos.

# Ferramentas do Projeto
* Dia - editor de diagramas:
* Br Modelo - banco de dados:
* Pencil Project - editor de telas:
* Visual Code - editor de programação

# Configuração Inicial

## Ambiente virtual para desenvolvimento
* Abrir terminal
* Entrar na pasta pi3b12024 com o comando: cd 
* Criar ambiente virtual com o comando: virtualenv .venv
* Ativar ambiente .venv com o comando: Linux -> source .venv/bin/activate, para desativar: deactivate
* No ambiente virtual .venv inicializar o Django: pip install django
* Utilize o comando, pip freeze, para saber a versão do django.
* Criar setup Django: django-admin startproject escolaativa
* Executar o comando: python3 manage.py migrate, este comando vai inicializar os módulos.
* Executar o comando: python3 manage.py runserver, este comando vai abrir a página.