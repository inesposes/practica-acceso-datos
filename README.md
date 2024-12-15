# Ejercicio: Desarrollo e integración de scripts en Python

## Descripción del proyecto

El objetivo de este ejercicio es desarrollar dos scripts en Python que interactúen con una API, una base de datos MongoDB y diversas herramientas para el manejo de datos. Además, el proyecto incluye opciones avanzadas para mejorar la funcionalidad e integración de la solución.

La API seleccionada para el ejercicio es la de [Citybikes](https://citybik.es/), que proporciona información en tiempo real sobre el estado de las estaciones de bicicletas de alquiler en varias ciudades del mundo.

---

## Estructura del proyecto

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

## Scripts

### api_bikes.py
- **Funcionalidad:**
  - Se conecta a la API de citybik.es cada 5 minutos e inserta los datos sobre las estaciones en una base de datos mongo.
  - Se ejecuta de forma continua hasta que se cancela manualmente.
- **Ejecución:**
   - Este script ya se encuentra corriendo en una instancia de OpenStack. Se ha creado una imagen (véase Dockerfile) a partir de él que está disponible en DockerHub (https://hub.docker.com/r/inesposes/practica-acceso-datos). Esta imagen se ha incluído en el docker-compose.yml, en el cual se levanta el servicio de la base de datos Mongo y el servicio que corre el script mencionado.
### api_news.py
- **Funcionalidad:**
  - Lee los datos almacenados en la base de datos MongoDB y los carga en un dataframe de Pandas.
  - Exporta los siguientes campos en dos formatos (CSV y Parquet):
- **Ejecución:**
   - pip install -r requirements/requirements.txt
   - Necesaria conexión a la VPN del Cesga en la que se está ejecutando el script para poder hacer una inserción de datos contra la base de datos que está levantada en el servidor mencionado anteriormente.
   - En local: python api_news.py

### file_export.py
- **Funcionalidad:**
  - Lee los datos almacenados en la base de datos MongoDB y los carga en un dataframe de Pandas.
  - Exporta los siguientes campos en dos formatos (CSV y Parquet):
    - `id`, `name`, `timestamp`, `free_bikes`, `empty_slots`, `uid`, `last_updated`, `slots`, `normal_bikes`, `ebikes`.
  - Los exporta en la carpeta datasets en la que ahora mismo hay dos de ejemplo.
- **Ejecución:**
---

## Parte avanzada (opcional)

### Funcionalidades implementadas
1. **Dockerización:**
   - El primer script se ejecuta dentro de un contenedor Docker.
2. **Servidor MongoDB:**
   - Se utiliza un servidor MongoDB propio ejecutado en un contenedor Docker.
3. **Publicación en Docker Hub:**
   - Imagen Docker publicada en Docker Hub.
4. **Despliegue en OpenStack:**
   - Configuración y ejecución de la aplicación en cloud usando Docker.
5. **Automatización:**
   - Actualización automática del contenedor Docker mediante cambios en el repositorio de GitHub.
6. **Extra:**
   - Creación de un sistema adicional para consultar y almacenar datos de una nueva API de interés.

---

## Instrucciones de ejecución

### Requisitos previos
- **Python 3.8+**
- **MongoDB**
- **Docker y Docker Compose**

### Instalación de dependencias

```bash
pip install -r requirements.txt
```

### Ejecución de los scripts

#### Script 1
```bash
python scripts/script1.py
```

#### Script 2
```bash
python scripts/script2.py
```

### Dockerización

#### Construir la imagen Docker
```bash
docker build -t citybikes-script .
```

#### Ejecutar el contenedor
```bash
docker-compose up
```

---

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más información.


