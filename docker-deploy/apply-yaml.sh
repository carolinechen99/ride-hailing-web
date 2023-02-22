#!/bin/bash

# Define the order of YAML files
YAML_FILES=(
    data-volume-persistentvolumeclaim.yaml
    db-deployment.yaml
    docker-deploy-default-networkpolicy.yaml
    web-claim0-persistentvolumeclaim.yaml
    nginx-claim0-persistentvolumeclaim.yaml
    web-init-claim0-persistentvolumeclaim.yaml
    web-init-deployment.yaml
    web-deployment.yaml
    nginx-deployment.yaml
    web-service.yaml
    nginx-service.yaml
)

# Loop through the YAML files and apply them in order
for file in "${YAML_FILES[@]}"; do
    kubectl apply -f "$file"
done
