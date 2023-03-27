#!/bin/bash

# Define the Azure Container Registry name
ACR_NAME=riderepo

# Authenticate Docker with Azure Container Registry
docker login $ACR_NAME.azurecr.io

# Define the list of Docker images to push
IMAGES=(
    docker-deploy-web
    docker-deploy-web-init
    postgres
    nginx
)

# Loop through the Docker images and push them to Azure Container Registry
for IMAGE in "${IMAGES[@]}"; do
    # Tag the Docker image with Azure Container Registry name and version
    docker tag $IMAGE $ACR_NAME.azurecr.io/$IMAGE:latest

    # Push the Docker image to Azure Container Registry
    docker push $ACR_NAME.azurecr.io/$IMAGE:latest
done
