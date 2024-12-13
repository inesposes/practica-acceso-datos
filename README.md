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

## Parte básica

### Script 1
- **Funcionalidad:**
  - Se conecta a la API de Citybikes a intervalos regulares configurables.
  - Obtiene datos de la API y los almacena en una base de datos MongoDB.
  - Se ejecuta de forma continua hasta que se cancela manualmente.

### Script 2
- **Funcionalidad:**
  - Lee los datos almacenados en la base de datos MongoDB y los carga en un dataframe de Pandas.
  - Exporta los siguientes campos en dos formatos (CSV y Parquet):
    - `id`, `name`, `timestamp`, `free_bikes`, `empty_slots`, `uid`, `last_updated`, `slots`, `normal_bikes`, `ebikes`.

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

## Documentación

- [Guía de ejecución](docs/guía_ejecución.md)
- [Referencias y recursos adicionales](docs/referencias.md)

---

## Criterios de evaluación

1. **Funcionamiento correcto:**
   - Verificación de que los scripts cumplen con las especificaciones del enunciado.
2. **Calidad del código:**
   - Buena estructura, uso de buenas prácticas y comentarios adecuados.
3. **Documentación:**
   - El README.md debe ser claro, completo y útil para usuarios nuevos.
4. **Control de errores:**
   - Manejo robusto de errores de conectividad y ejecución.
5. **Funcionalidades avanzadas:**
   - Implementación correcta y clara de las opciones avanzadas y extra.

---

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más información.


