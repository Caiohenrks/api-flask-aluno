# API de Alunos

Esta API permite o gerenciamento de usuários e alunos, oferecendo operações de CRUD para ambas as entidades.

## Bibliotecas Utilizadas

- Flask 2.3.3: Microframework para desenvolvimento web em Python.
- Flask-Smorest 0.42.1: Extensão para facilitar a criação de APIs RESTful com Flask e Marshmallow.
- Flasgger 0.9.7.1: Ferramenta para extração de especificações Swagger e criação de Swagger UI a partir do código Flask.
- Flask-SQLAlchemy 3.1.1: Extensão para Flask que adiciona suporte para SQLAlchemy.
- Authlib 1.2.1: Biblioteca para construção de servidores e clientes OAuth e OpenID Connect.
- Werkzeug 2.3.7: Biblioteca WSGI abrangente para aplicações web em Python.
- Flask-HTTPAuth 4.8.0: Extensão para Flask que fornece autenticação HTTP básica.

## Consumindo API via CURL

1. Cadastrar Usuário
`curl -X POST -H "Content-Type: application/json" -d "{\"username\": \"usuario_teste\", \"password\": \"senha_segura\"}" http://127.0.0.1:5000/cadastrar_usuario
2. Cadastrar Aluno
`curl -X POST -u usuario_teste:senha_segura -H "Content-Type: application/json" -d "{\"nome\": \"João Silva\", \"av1\": 8.5, \"av2\": 7.5, \"av3\": 9.0, \"av4\": 10.0}" http://127.0.0.1:5000/cadastrar_aluno`
3. Listar Alunos
`curl -X GET -u usuario_teste:senha_segura http://127.0.0.1:5000/alunos`
4. Obter um Aluno
`curl -X GET -u usuario_teste:senha_segura http://127.0.0.1:5000/aluno/1`
5. Atualizar Aluno
`curl -X PUT -u usuario_teste:senha_segura -H "Content-Type: application/json" -d "{\"nome\": \"João Pereira\", \"av1\": 9.0, \"av2\": 8.5, \"av3\": 9.5, \"av4\": 10.0}" http://127.0.0.1:5000/aluno/1`
6. Deletar Aluno
`curl -X DELETE -u usuario_teste:senha_segura http://127.0.0.1:5000/aluno/1`


### Criação da tabela


```SQL
CREATE DATABASE IF NOT EXISTS mysqldb;

USE mysqldb;

CREATE TABLE IF NOT EXISTS usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS aluno (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    av1 FLOAT NOT NULL,
    av2 FLOAT NOT NULL,
    av3 FLOAT NOT NULL,
    av4 FLOAT NOT NULL
);
```


### Configuração do banco

#### mysql
`MYSQL_ROOT_PASSWORD: q1w2e3r4t5`
`MYSQL_DATABASE: mysqldb`
`MYSQL_USER: caiohenrks`
`MYSQL_PASSWORD: 12345678`

#### phpmyadmin
`PMA_HOST: mysql`
`PMA_USER: root`
`PMA_PASSWORD: q1w2e3r4t5`
