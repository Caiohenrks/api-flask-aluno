#!/bin/bash

# Definir o nome ou ID do container MySQL
CONTAINER_NAME="mysql"

# Definir o script SQL
SQL_SCRIPT="
CREATE DATABASE IF NOT EXISTS mysqldb;
CREATE USER IF NOT EXISTS 'caiohenrks'@'%' IDENTIFIED BY '12345678';
GRANT ALL ON mysqldb.* TO 'caiohenrks'@'%';
FLUSH PRIVILEGES;
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
"

# Escrever o script SQL para um arquivo temporário
echo "$SQL_SCRIPT" > temp.sql

# Copiar o script SQL para o container
docker cp temp.sql $CONTAINER_NAME:/tmp/temp.sql

# Executar o script SQL dentro do container
docker exec $CONTAINER_NAME bash -c "mysql -u root -pq1w2e3r4t5 < /tmp/temp.sql"

# Remover o arquivo temporário
rm temp.sql

echo "Banco de dados e tabelas criados com sucesso no container $CONTAINER_NAME!"

