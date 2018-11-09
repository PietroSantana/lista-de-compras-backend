# lista-de-compras-backend
Backend do Projeto Lista de Compras para a disciplina PCS3643 - 2018

Clonar o projeto através da linha de comando

Entrar no diretório do Projeto

Criar um ambiente virtual de python para o projeto 
pip install virtualenv

virtualenv --version

virtualenv venv
virtualenv my_project will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages. The name of the virtual environment (in this case, it was my_project) can be anything; omitting the name will place the files in the current directory instead.

Abrir o editor vscode

Escolher o interprete do Python que está no venv

Abrir um terminal do vscode
Verificar que o ambiente virtual venv está selecionado, se não, selecionar ele.

Instalar as dependências via 
pip3 install -r requirements.txt

Executar o projeto via 
python app.py

Abrir o Postman
Criar requisições para teste da API

POST
url: http://127.0.0.1/item

Headers
key:Content-Type
value:application/json
Body
raw
{"item":"abobora"}

GET
url: http://127.0.0.1/itens/abobora

PUT
url: http://127.0.0.1/item

Headers
key:Content-Type 
value:application/json
Body
raw
{"item":"tomates"}

GET
url: http://127.0.0.1/itens

DELETE
url: http://127.0.0.1/item/abobora

