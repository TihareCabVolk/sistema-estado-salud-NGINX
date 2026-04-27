# sistema-estado-salud-NGINX
Este repositorio se basa en el uso de NGINX para realizar un análisis y empleamiento de este.

# Actualizar los repositorios
sudo apt update

# Instalar Git, Docker y Docker Compose
sudo apt install -y git docker.io docker-compose-v2

# Clonar el repositorio 
git clone https://github.com/TihareCabVolk/sistema-estado-salud-NGINX.git

# Entrar a la carpeta del proyecto
cd sistema-estado-salud

# Para ejecutar el codigo con Docker en la VM
docker compose up --build -d