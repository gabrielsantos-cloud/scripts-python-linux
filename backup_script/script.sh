#!/bin/bash
python3 backup.py

echo "Conteúdo do diretório /script/backup:\""

mkdir arquivos_compactados

mv backup_* arquivos_compactados

cd arquivos_compactados

tar -xvf backup_* > retorno.txt

echo "Retorno após descompactar o arquivo .tar"

cat retorno.txt

echo "Arquivos que estavam no seu arquivo compactado .tar"

cd backup 

ls 



