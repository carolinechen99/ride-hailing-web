## Docker
The docker-deploy folder contains the Dockerfile and the docker-compose.yml file to build and run the docker image.

We first need to build the docker image. The docker-compose.yml file contains the build instructions. We can build the docker image by running the following command:

```bash
docker-compose up
```

We then push docker images to Azure Container Registeries (ACR) by running the following command:

```bash
./push-docker.sh
```

## Kubernetes


Having a docker image is not enough to run it in a Kubernetes cluster. The kubernetes folder contains the deployment and service files to run the docker image in a Kubernetes cluster.

Make sure you have a Kubernetes cluster running. If you don't have a Kubernetes cluster, you can use minikube to run a Kubernetes cluster locally.

Here we are using minikube to run a Kubernetes cluster locally. To start minikube, run the following command:

```bash
minikube start --driver docker
```
which will start a Kubernetes cluster using the docker driver. The docker driver will use the docker daemon running on the host machine. The docker driver is the default driver for minikube.

Check minikube status by running the following command:

```bash
minikube status
```

We first need to create the deployment and service files. We utilize kompose to convert the docker-compose.yml file to the deployment and service files. 

```bash
kompose convert -f docker-compose.yml
``` 
The above command will create the deployment and service files. We can then deploy the docker image to the Kubernetes cluster.

The order of deployment is important since dependencies exist between the services. We have created a script called 'apply-yaml' to which run `kubectl apply -f` on the deployment and service files in the correct order. To deploy the services, run the following command:

```bash
./apply-yaml.sh
```

## Checking the status and Debugging

Once you have applied all the YAML files, you can check the status of your deployments and services using kubectl get commands.
    
    ```bash
    kubectl get deployments
    kubectl get services
    ```
This will give you a list of all the services in your cluster, along with information about the service type, cluster IP, and external endpoints.

To see more detailed information about a specific deployment or service, you can use kubectl describe. For example, to see more information about the nginx, run the following command:

```bash
kubectl describe service nginx
```
- Use the `kubectl describe pod <pod_name>` command to get more information about the pods and check for any errors or issues

- Additionally, you can check the logs of the containers using the `kubectl logs <pod_name>` command to debug the issues.

- To check the status of the cluster components, use the command `kubectl get componentstatuses`. This will show you the health of the various components of the cluster such as the API server, controller manager, and etcd.

- To get a list of all the nodes in the cluster, use the command `kubectl get nodes `. This will show you information about the nodes such as their status, IP address, and version.

- To get a list of all the pods in the cluster, use the command `kubectl get pods`. This will show you information about the pods such as their status, IP address, and the node they are running on.

- To get a list of all the services in the cluster, use the command `kubectl get services`. This will show you information about the services such as their type, IP address, and the port they are running on.

- To get a list of all the deployments in the cluster, use the command `kubectl get deployments`. This will show you information about the deployments such as their status, the number of replicas, and the strategy used.

- You can try to check the status of the Kubernetes cluster and ensure that it is running by running the following command:
    
    ```bash
    kubectl cluster-info
    ```