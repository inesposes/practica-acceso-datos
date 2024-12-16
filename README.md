# Ejercicio: Desarrollo e integración de scripts en Python

## 📜 Descripción del proyecto

Este proyecto forma parte de una entrega para la asignatura Sistemas de Big Data del curso de especialización en IA y Big Data.

El objetivo de este ejercicio es desarrollar un script de  Python que interactúe con una API y que posteriormente introduzcan los datos en una base de datos MongoDB. Por último, se ha añadido un script que permite exportar un .csv y un .parquet de los datos que han sido guardados en este tiempo.

La API seleccionada para el ejercicio es la de [Citybik.es](https://citybik.es/), que proporciona información en tiempo real sobre el estado de las estaciones de bicicletas de alquiler en varias ciudades del mundo. He utilizado los datos para la ciudad de A Coruña.

Adicionalmente, se ha realizado un script que consulta una API de noticias [NewsAPI](https://newsapi.org/) y los inserta en una base de datos MongoDB.

> Se presupone que para este trabajo se tiene una conexión a una VPN del CESGA, gracias a unos credenciales proporcionados con propósito académico.  No obstante, se incluyen todas las explicaciones para poder probarlo en local.
---

## 📁 Estructura del proyecto

```plaintext
📂 practica-acceso-datos
├── 📁 datasets
│   ├── stations.csv
│   ├── stations.parquet
├── 📁 scripts
│   ├── api_bikes.py
│   ├── api_news.py
│   ├── file_export.py
├── 🐳 docker-compose.yml
├── 🐳 Dockerfile
├── 🛠️env.example
├── 📄README.md
├── 📦requirements.txt
```

---

## 📝Scripts

###  ⚙️Requisitos previos a la ejecución de los scripts
- git clone https://github.com/inesposes/practica-acceso-datos
- Python 3.8+
- Instalación de dependencias: ```pip install -r requirements.txt```

### 🚴‍♂️api_bikes.py
- **Funcionalidad:**
  - Se conecta a la API de citybik.es cada 5 minutos e inserta los datos sobre las estaciones en una base de datos MongoDB.
  - Se ejecuta de forma continua hasta que se cancela manualmente.
  - Un ejemplo de datos de una estación:
    ```json
    {
      "_id": {
        "$oid": "676070ad97fa852f8e0f8c20"
      },
      "id": "447505d0e57db2f71d7572ceedcbb046",
      "name": "Agrela",
      "latitude": 43.354365513765316,
      "longitude": -8.422193301049806,
      "timestamp": "2024-12-16T18:24:33.037331Z",
      "free_bikes": 1,
      "empty_slots": 22,
      "extra": {
        "uid": "28",
        "renting": true,
        "returning": true,
        "last_updated": 1734373350,
        "address": "Rúa Gutemberg, 16 ",
        "post_code": "15008",
        "payment": ["key", "transitcard", "creditcard", "phone"],
        "payment-terminal": true,
        "altitude": 0,
        "slots": 23,
        "normal_bikes": 0,
        "ebikes": 1,
        "has_ebikes": true,
        "rental_uris": {}
      }
    }

    ```
- **Ejecución:**
   - Necesaria conexión a la VPN CESGA. Este script ya se encuentra corriendo en una instancia de OpenStack del CESGA. 
      - Se ha creado una imagen (véase Dockerfile) que está disponible en   [DockerHub](https://hub.docker.com/r/inesposes/practica-acceso-datos). 
      - Se ha configurado un workflow en Github para que cada vez que se hagan cambios en la imagen estos se actualicen instantáneamente en DockerHub
      - Esta se ha utilizado en el docker-compose.yml, en el cual se levanta el servicio de la base de datos Mongo y el servicio que corre el script mencionado.
   - Si se quiere probar en local, hay que ejecutar el siguiente comando. El script empezaría a ejecutarse automáticamente.
      ```bash
        docker-compose up -d
      ```
### 📰 api_news.py
- **Funcionalidad:**
  - Se conecta a la API de newsapi.org una vez al día y recoge 100 noticias que incluyan la palabra 'Tech' que hayan sido publicadas entre ese día y el día anterior.
  - Se ejecuta de forma continua hasta que se cancela manualmente.
  - Un ejemplo de noticia insertada:
  ```json
   {
    {
      "_id": {
        "$oid": "6760710c16c1a2e28d5dfe6f"
      },
      "source": {
        "id": null,
        "name": "Digital Trends"
      },
      "author": "Nirave Gondhia",
      "title": "I tried the Dexcom Stelo, one of the best mobile gadgets for tracking your glucose",
      "description": "CGMs have saved my life after a heart attack four years ago. I recently tried the Dexcom Stelo OTC CGM, and it's been mighty impressive.",
      "url": "https://www.digitaltrends.com/mobile/i-tried-dexcom-stelo-one-of-the-best-mobile-gadgets-for-tracking-your-glucose/",
      "urlToImage": "https://www.digitaltrends.com/wp-content/uploads/2024/11/dexcom-stelo-photography-pred-makinglunch-sensor-closeup-1201x901-1c7b5e7.jpg?resize=1200%2C630&p=1",
      "publishedAt": "2024-12-15T12:30:02Z",
      "content": "Table of Contents\nTable of Contents\nWhy a great CGM is so valuable to diabetics\nA brief look at my CGM history\nWhy the Dexcom Stelo is great for most people\nThe key differences between the Dexco… [+8002 chars]"
    }
  }

  ```

- **Ejecución:**
   - Es necesario que tengas una API key que puedes solicitar en este [enlace](https://newsapi.org/register). 
   - Seguidamente, crea un .env con los datos del env.example y cubre "NEWS_API_KEY" con tu API key
   - Desde el directorio raíz de este proyecto: python scripts/api_news.py
   - Nota: si se ha levantado el servidor MongoDB en local es necesario cambiar la IP que hay dentro del script por 'mongo_db'

### 📥file_export.py
- **Funcionalidad:**
  - Si no se tiene conexión a la VPN del CESGA, es necesario cambiar la IP de dentro del script por 'mongo_db', para que consulte al Docker levantado en local.
  - Lee los datos almacenados en la base de datos MongoDB 'bicicorunha' y los carga en un dataframe de Pandas.
  - Exporta los siguientes campos en dos formatos (CSV y Parquet):
    - `id`, `name`, `timestamp`, `free_bikes`, `empty_slots`, `uid`, `last_updated`, `slots`, `normal_bikes`, `ebikes`.
  - Los exporta en la carpeta datasets en la que ahora mismo hay dos de ejemplo.
- **Ejecución:**
   - Desde el directorio raíz de este proyecto: python scripts/file_export.py


