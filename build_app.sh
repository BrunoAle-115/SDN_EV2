#!/bin/bash

# Nombre de la imagen y contenedor
IMAGE_NAME="sdn_ev2_app"
CONTAINER_NAME="contenedor_bruno"

echo "Iniciando proceso de automatización para $IMAGE_NAME..."

# 0. Limpieza: Eliminar contenedor anterior si existe para evitar conflictos
docker rm -f $CONTAINER_NAME 2>/dev/null || true

# 1. Crear Dockerfile (Requerimiento D)
cat << EOF > Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
CMD ["python", "app.py"]
EOF

# 2. Construir Imagen
docker build --no-cache -t $IMAGE_NAME .

# 3. Correr Contenedor (Pasando la variable de entorno del sistema)
docker run --name $CONTAINER_NAME -e API_KEY_NASA="$API_KEY_NASA" $IMAGE_NAME

# 4. Generar Evidencia (Requerimiento D) en la carpeta correcta
# Aseguramos que el directorio exista
mkdir -p evidencias/docker
echo "--- Registrando Output ---" > evidencias/docker/output.txt
docker ps -a --filter "name=$CONTAINER_NAME" >> evidencias/docker/output.txt
echo "--- Logs de la App ---" >> evidencias/docker/output.txt
docker logs $CONTAINER_NAME >> evidencias/docker/output.txt

echo "Proceso finalizado. Archivo output.txt generado en evidencias/docker/."