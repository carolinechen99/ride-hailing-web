## Docker
The docker-deploy folder contains the Dockerfile and the docker-compose.yml file to build and run the docker image.

We first need to build the docker image. The docker-compose.yml file contains the build instructions. We can build the docker image by running the following command:

```bash
docker-compose up
```

## Kubernetes


Having a docker image is not enough to run it in a Kubernetes cluster. The kubernetes folder contains the deployment and service files to run the docker image in a Kubernetes cluster.

Make sure you have a Kubernetes cluster running. If you don't have a Kubernetes cluster, you can use minikube to run a Kubernetes cluster locally.

Here we are using minikube to run a Kubernetes cluster locally. To start minikube, run the following command:

```bash
minikube start --driver docker
```
which will start a Kubernetes cluster using the docker driver. The docker driver will use the docker daemon running on the host machine. The docker driver is the default driver for minikube.

We first need to create the deployment and service files. We utilize kompose to convert the docker-compose.yml file to the deployment and service files. 

```bash
kompose convert -f docker-compose.yml
``` 
The above command will create the deployment and service files. We can then deploy the docker image to the Kubernetes cluster.

The order of deployment is important since dependencies exist between the services. We have created a script called 'apply-yaml' to deploy the services in the correct order. To deploy the services, run the following command:

```bash
./apply-yaml.sh
```





