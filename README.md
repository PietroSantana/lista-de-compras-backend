# lista-de-compras-backend
Backend do Projeto Lista de Compras para a disciplina PCS3643 - 2018

## Instalação
Este projeto precisa de python 3 instalado. Nas máquinas do Labprog, o path está em
```'C:\Program Files\Python37\'
```

Clonar o projeto através da linha de comando
```
git clone https://github.com/miklt/lista-de-compras-backend.git
```

Entrar no diretório do Projeto
```
cd lista-de-compras-backend
```
Instalar o virtualenv, para criar um ambiente python para o projeto 
```
pip3 install virtualenv --user
```
Verificar se o virtualenv foi instalado e está no seu path
```
virtualenv --version
```
Se não aparecer, significa que o virtualenv não foi adicionado ao seu path, mas ele deve estar instalado no seu perfil neste path:
``` 
'c:\users\aluno\appdata\roaming\python\Python37\Scripts\virtualenv.exe' 
``` 
 onde aluno é o usuário atual.

Então você pode executar o seguinte comando:
```
virtualenv -p python3 env
```

Ou:
```
c:\users\aluno\appdata\roaming\python\Python37\Scripts\virtualenv.exe -p "c:\Program Files\Python37\python.exe" env 
```
(lembre-se de substituir seu nome de usuário por 'aluno' caso seja necessário.

Depois é preciso ativar o ambiente virtual
Para isso, no windows, execute o seguinte comando:
```
env\Scripts\activate.bat
```

Instalar as dependências via 
```
pip3 install -r requirements.txt
```

Executar o projeto via 
```
python app.py
```

Para testar, é possível utilizar o Postman ou testar usando o Frontend do projeto.

Abrir o Postman
Criar requisições para teste da API

POST
url: http://127.0.0.1:5000/item

Headers
key:Content-Type
value:application/json
Body
raw
{"item":"abobora"}

GET
url: http://127.0.0.1:5000/item/abobora

PUT
url: http://127.0.0.1:5000/item

Headers
key:Content-Type 
value:application/json
Body
raw
{"item":"tomates"}

GET
url: http://127.0.0.1:5000/itens

DELETE
url: http://127.0.0.1:5000/item/abobora

