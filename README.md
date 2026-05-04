# Sistema de Estado de Salud - NGINX

Este repositorio demuestra el diseño y despliegue de una arquitectura de alta disponibilidad para un centro de salud, utilizando NGINX como balanceador de carga para distribuir el tráfico y evitar caídas del sistema.

## Arquitectura del Sistema

El sistema distribuye las peticiones equitativamente (algoritmo Round-Robin) entre múltiples réplicas de la aplicación, compartiendo una base de datos ultrarrápida.

## Actualizar los repositorios
sudo apt update

## Instalar Git, Docker y Docker Compose
sudo apt install -y git docker.io docker-compose-v2

## Clonar el repositorio 
git clone https://github.com/TihareCabVolk/sistema-estado-salud-NGINX.git

## Entrar a la carpeta del proyecto
cd sistema-estado-salud

## Ejecutar el codigo con Docker en la VM y reconstruir la imagen de Docker
docker compose up --build -d

## Ver los registros de todos los contenedores en tiempo real
docker compose logs -f

## Ver estado de contenedores
docker compose ps


## Arquitectura del Sistema

```mermaid
graph TD
    A[Usuario / Cliente] -->|Petición GET/POST al Puerto 80| B(NGINX\nBalanceador de Carga)
    
    B -->|Distribuye vía Round-Robin| C[Réplica Flask 1\nPuerto Interno: 3001]
    B -->|Distribuye vía Round-Robin| D[Réplica Flask 2\nPuerto Interno: 3002]
    B -->|Distribuye vía Round-Robin| E[Réplica Flask 3\nPuerto Interno: 3003]
    
    C -->|Operaciones Atómicas| F[(Redis\nBase de Datos en Memoria)]
    D -->|Operaciones Atómicas| F
    E -->|Operaciones Atómicas| F

