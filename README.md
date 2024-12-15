# Ejercicio: Desarrollo e integración de scripts en Python

## 📜 Descripción del proyecto

El objetivo de este ejercicio es desarrollar dos scripts en Python que interactúen con dos APIs que posteriormente introduzcan los datos en una base de datos MongoDB. Por último, se ha añadido un script que permite exportar un .csv y un .parquet de los datos que han sido guardados en este tiempo.

La API seleccionada para el ejercicio es la de [Citybikes](https://citybik.es/), que proporciona información en tiempo real sobre el estado de las estaciones de bicicletas de alquiler en varias ciudades del mundo, pero he utilizado los datos de la API de Coruña.

---

## 📁 Estructura del proyecto

```plaintext
📂 practica-acceso-datos
├── 📁 datasets
│   ├── stations.csv
│   ├── stations.parquet
├── 📁 requirements
│   ├── requirements.txt
│   ├── requirements_optional.txt
├── 📁 scripts
│   ├── api_bikes.py
│   ├── api_news.yml
│   ├── file_export.yml
├── 🐳 Dockerfile
├── 🐳 docker-compose.yml
├── 📄 README.md
```

---

## 📝Scripts

###  ⚙️Requisitos previos a la ejecución de los scripts
- **Python 3.8+**
- Instalación de dependencias: ```pip install -r requirements.txt```
- Necesaria conexión a la VPN del CESGA en la que se está ejecutando el script para poder hacer una inserción de datos contra la base de datos que está levantada en el servidor mencionado anteriormente.
- En caso de tener opción de conectarse a ese servidor del CESGA se puede levantar el servidor en local haciendo:
```bash
docker-compose up
```
- Seguidamente habría que en los scripts la ip del servidor remoto por mongo_db (nombre del servidor levantado en local)

### 🚴‍♂️api_bikes.py
- **Funcionalidad:**
  - Se conecta a la API de citybik.es cada 5 minutos e inserta los datos sobre las estaciones en una base de datos mongo.
  - Se ejecuta de forma continua hasta que se cancela manualmente.
- **Ejecución:**
   - Este script ya se encuentra corriendo en una instancia de OpenStack. Se ha creado una imagen (véase Dockerfile) que está disponible en   [DockerHub](https://hub.docker.com/r/inesposes/practica-acceso-datos). Esta se ha utilizado en el docker-compose.yml, en el cual se levanta el servicio de la base de datos Mongo y el servicio que corre el script mencionado.
### 📰 api_news.py
- **Funcionalidad:**
  - Se conecta a la API de newsapi.org una vez al día y recoge 100 noticias que incluyan la palabra 'Tech' que hayan sido publicadas entre ese día y el día anterior.
- **Ejecución:**
   - Desde el directorio raíz de este proyecto: python scripts/api_news.py

### 📥file_export.py
- **Funcionalidad:**
  - Lee los datos almacenados en la base de datos MongoDB y los carga en un dataframe de Pandas.
  - Exporta los siguientes campos en dos formatos (CSV y Parquet):
    - `id`, `name`, `timestamp`, `free_bikes`, `empty_slots`, `uid`, `last_updated`, `slots`, `normal_bikes`, `ebikes`.
  - Los exporta en la carpeta datasets en la que ahora mismo hay dos de ejemplo.
- **Ejecución:**
   - Desde el directorio raíz de este proyecto: python scripts/api_news.py

---

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más información.


