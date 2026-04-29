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

# Para ejecutar el codigo con Docker en la VM y tambien reconstruir la imagen del Docker
docker compose up --build -d

# Para ver los Logs de todos los contenedores
docker compose logs -f

```mermaid
graph TD
    A[Usuario / Cliente] -->|Petición GET/POST al Puerto 80| B(NGINX\nBalanceador de Carga)
    
    B -->|Distribuye vía Round-Robin| C[Réplica Flask 1\nPuerto Interno: 3001]
    B -->|Distribuye vía Round-Robin| D[Réplica Flask 2\nPuerto Interno: 3002]
    B -->|Distribuye vía Round-Robin| E[Réplica Flask 3\nPuerto Interno: 3003]
    
    C -->|Operaciones Atómicas| F[(Redis\nBase de Datos en Memoria)]
    D -->|Operaciones Atómicas| F
    E -->|Operaciones Atómicas| F
