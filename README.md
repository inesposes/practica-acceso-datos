# practica-acceso-datos
Práctica final da avaliación de SBD



1. 
Hay un env_conf.yml para crear una configuración de un environment conda. Ejecutar los siguientes comandos:
conda env create --file env_conf.yml
conda activate acceso-datos


2. docker image
docker tag 801eea734ec6 inesposes/mongo-data-inserter:latest
docker push inesposes/mongo-data-inserter:latest

3. docker compose
docker

4. pip list --format=freeze > requirements.txt