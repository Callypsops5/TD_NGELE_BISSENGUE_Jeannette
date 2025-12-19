Write-Host "=== DEPLOIEMENT DAILYHABITS ===" -ForegroundColor Cyan

# Stop en cas d’erreur
$ErrorActionPreference = "Stop"

# Variables
$API_IMAGE = "jeannette329/dailyhabits-api:1.1"
$FRONT_IMAGE = "jeannette329/dailyhabits-frontend:1.1"

Write-Host "1) Vérification de docker-compose.yml"
docker compose config

Write-Host "2) Build des images"
docker build -t $API_IMAGE ./api
docker build -t $FRONT_IMAGE ./frontend

Write-Host "3) Tests unitaires API"
docker run --rm $API_IMAGE pytest

Write-Host "4) Connexion au registre Docker Hub"
docker login

Write-Host "5) Push des images vers Docker Hub"
docker push $API_IMAGE
docker push $FRONT_IMAGE

Write-Host "6) Déploiement avec Docker Compose"
docker compose up -d --build

Write-Host "=== DEPLOIEMENT TERMINE AVEC SUCCÈS ===" -ForegroundColor Green
