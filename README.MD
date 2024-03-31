# Bem vindo!

# Índice
* [Apresentação do Projeto](#Apresentação-do-Projeto)
* [Ferramentas do Projeto](#Ferramentas-do-Projeto)
* [Configuração Inicial](#Configuração-Inicial)
* [Django Framework](#Django-Framework)

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

# Django Framework
## MTV Model, Template e View

### Model
Parte da aplicação que se comunica com o SGBD por meio de mapeamento objeto-relacional do Django.

### Template
É a parte que o usuário visualiza, a <b>camada de apresentação</b> do sistema escrito em Django.

### View
Corresponde à camada que controla a interação entre os dados (Model) e a apresentação (Template). São as regras de neǵocios da aplicação.

## Criando um Novo Projeto em Django
Primeiro devemos criar um ambiente virtual. 

### Linux - Ambiente Virtual
* Verificar instalação do Python com o comando <b>which python</b>.
* Verificar versão do Python com o comando <b>python3 -V</b>
* Caso não tiver o Python instalado utilizar o comando <b>sudo apt-get install python3.9.2</b>
* Instalar gerenciador de pacotes pip com o comando <b>sudo apt-get install python3-pip</b>
* Criar ambiente virtual dentro da pasta do projeto digite o comando <b>python3 -m pip install virtualenv</b>
* Crie uma pasta para o projeto e digite o comando <b>virtualenv .venv</b>
* Utilize o comando <b>source .venv/bin/activate</b> para ativar o ambiente virtual.

### Instalando o Django
* Digite o comando <b>python3 -m pip install Django==4.2.11</b>
* Digite <b>django-admin startproject escolaativa</b>

### Inicializando o Servidor
* Digite <b>cd escolaativa</b> para entrar na pasta do projeto django.
* Digite <b>./manage.py migrate</b> para inicializar os módulos.
* Digite <b>./manage.py runserver</b> para inicializar o servidor com a página web.
* No navegador entre no endereço <b>http://127.0.0.1:8000/</b>
