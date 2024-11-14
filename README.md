## PostgreSQL Cluster Deployment on Minikube ##

## Overview ##
This project demonstrates the deployment of a PostgreSQL cluster on Minikube, including a load balancer (HAProxy), asynchronous replication to a standalone PostgreSQL node, and automated data population using the Faker library.

## Architecture
Attached.

-- Below is a URL as well:

https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&target=blank&highlight=0000ff&edit=_blank&layers=1&nav=1&title=PostgreSQL%20Cluster%20using%20Minikube.drawio.drawio#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Page-1%22%20id%3D%221v75MXz2L22W5dkLzYuI%22%3E7Vtdc%2Bo2EP01eWxGtmwDj4GQm95JOvTSmdv2JSOwYtTIFpFFgP76SlgGy7KB1AHyQTIh1moly3uOVquVuYC9ePGNo%2BnknoWYXrggXFzA6wvX7fie%2FFSCZSYIgJ8JIk7CTORsBEPyL9ZCoKUzEuLUUBSMUUGmpnDMkgSPhSFDnLO5qfbIqHnXKYqwJRiOEbWlP0koJpm07YON%2FBaTaJLf2QG6Jka5shakExSyeUEE%2BxewxxkT2VW86GGqbJfbJWt3U1O7HhjHidinwXcvvu9%2Fn7O%2FZ398i37t3S7hy%2FMvupcXRGf6ge9JQp5mI6wHLZa5JdI5iSlKZKk7nxCBh1M0VlVzibuUTURMZcmRl48sEUPdcF3OkHU8Wdb3xFzgRe3DOGsTSWphFmPBl1JFN8iNqlnlQF2eFzDKkZgU8AlyIdK8iNZdb0wnL7T1XmFJ37KkbcEnLMZqdEAagc0EJQnurXkLtKV6jDK%2BagDl740aQjfiKCR4U5ewFQ6PhNKCeq%2Fj%2BiuDp4KzJ1xSDlE6waG%2BkTI%2BkSy%2FQyNMBywlgrBE1o2YECwuKFxREqkKwRTISJfGciyYV6CuUXZLLFC3ROk0e9BHslDj6E4ZUb30X2Rnqe5ETpKpahAvIuVOLtE89S55mD5MWSoijtNn%2BkCSVKBkjB8QFfuyqZ78tRRrgbbBMejYHGu5NsVy2ZszDLYsRuFQOitdZFxMWMQSRPsbaZezWRKuYd%2Fo3DEF6Mrm%2F2Ahlho5NBPMhDW7p7rR%2FzCuHCyb8THepge1V0c8wts6hNVocUyRIC%2Fm6N7e9u0vbXuvoe1XTa84R8uCwmr%2Bp4WeB0qwmYBB2cmD0gK3Q9%2FzQQn3bAQbFqwfpQExOl%2BaGMEpiOG%2Fjhf%2BCWjhgS9Ni9YpaOF5JtCwtZ0XntNM%2FyhEyk1eiCtvrwacLZZ2ePm6AF2HavCAIZQbtAyLBXYE5fqBHUK1DxWkO55lTcuMpRgcgCDo9Woj4p2BNC1VrEPnbbF09eagFO2vfqxoX9YE7bbThfXbhlx8TbjsPRtWotzNurN8q%2BtWhOQJFnPGn9JLylD4MEJUxeK8GYtqYjvdjRmHezaJOhU7PXgoDkHvQ7l2uKdvz6zc1GdbTrMDDfB83%2BwgW0l0mxIwb%2BA9c%2Bqc5%2FtHmu%2BO%2F85mPLRIc4QZL03Il3%2Fq9qvCX6pw6efF60Wx8npZLA0wJ%2FLhFU5Gvicnc0zCkBpZoaM4mXz93RlANvZGjQB390jmRRLgae0U0OloNMrVwb6m3D4zQMeYGY5rTw2vVTE3PNc%2FlK0qTBWsEnMjysZPzzMmsGG5QIlkdSw5QCQXr2QtKPx5YLpYcRGMGA8Vg5WGdmUrE4YhSSLdUOvmncqrSP0fZOnC4e93UqlHZ6maCnpc8jGLQ8saNI2ma9LdsOD4KX5slq%2FMMKwnh0mNimDb8zo2NeQ%2BZuei%2FkNxOYko3k49x9%2FDLSMqsUiQwF3lIdNDLPt7RPnnXPz7ysW7W6kNyykf6Fvkq3J7rUOFBK0zwz4Xw5x259J%2FXxwLzhz7XByD78yJuSc5uyhRzBkhB7tV21q5E%2B9f3TTYluTzZdeu5FhZ7Wab0JOcKHxcsJoeWTYDyzmD9Rqwmh4jNgPrvM4eeZ09ahxX8WrYcVdZYPFrwEmMuH2CJ20hTGgs2GoTeVVJCtOjlGEtwg4OCUlQinuAjUhQgYh7METstx5%2F4CmVZpVC23MfDxX3iKhAc5a4wA5Gq0A5WJI997qVoNge%2BXOCYnuv0%2BNiL48bXOyDkc%2BJSzn%2FdHpU7BTnUC6tIaIqZHDBbyy03%2BD%2BqNhsPxMJ2uaZCOxUJKadY64v0HZXnyr63%2Fd1sX2j%2F5pjjQO%2FRNgxpzQsf31il36zt79kcfPVj0x98%2F0Z2P8P%3C%2Fdiagram%3E%3C%2Fmxfile%3E

## Prerequisites ##
- Server / Local Machine
- Minikube
- Helm
- Python with `psycopg2` and `faker` libraries
- Basic knowledge of Kubernetes, Helm and PostgreSQL


## Steps to Deploy ##

### 1. Install Minikube
- Follow these steps to install and configure Minikube on Ubuntu.
- This the version of my Ubuntu Server:

Distributor ID: Ubuntu
Description:    Ubuntu 22.04.5 LTS
Release:        22.04
Codename:       jammy

- Installation Steps:

- Create Minikube Directory and cd to it:
mkdir minikube
cd minikube/

- Curl to download the installation file/ media and install:

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

- Check version to confirm the installation was successful:
minikube version

- Install Docker so that it can be used as a driver by minikube. There are other drivers like, virtualbox or vmware but Docker is most prefered:

apt install docker.io

- We need to Create user that we will use to start and configure Minikube this is because docker(our choosen driver) reccomends that it's run by a Non-Root User.

useradd minikubeuser
usermod -aG docker minikubeuser

- Now su as that user and Start Minikube:

minikube start --cpus=2 --memory=4096 --disk-size=20g --driver=docker


### 2. Install Helm ##

   Install Helm to manage Kubernetes applications.

- Install Helm:

curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

- Verify Helm has been Installed:

helm version


### 3. Deploy PostgreSQL Cluster
   Use the provided Helm chart to deploy a PostgreSQL cluster with 1 primary and 3 replica nodes.

- We first need to add bitnami repo that will be used to provision the PostgreSQL Cluster

helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update

- Create a Custom Namespace that we will use for this project:

kubectl create namespace postgres

- Provision the PostgreSQL Cluster from the Helm Chart Postgresql-values.yaml file:
    - The postgresql-values.yaml chart is in the charts directory:

helm install postgresql-cluster bitnami/postgresql -f postgresql-values.yaml --namespace postgres

- Confirm pods have been Created and in Running State

kubectl get pods --namespace postgres

- Incase of any issue with the pods, check the logs:

kubectl logs <pod-name> -n postgres

- Incase of any changes to the postgresql-values.yaml, just upgrade the previous installation:

helm install postgresql-cluster bitnami/postgresql -f postgresql-values.yaml --namespace postgres

- To check if replication is active:

kubectl exec -it postgresql-cluster-0 -n postgres -- psql -U dba_admin -d testdb -c "SELECT * FROM pg_stat_replication;"

- You can also check the stateful configs and cofirm everything is okay:

kubectl describe statefulset postgresql-cluster-postgresql -n postgres



### 4. Set Up Load Balancer with HAProxy
   Deploy HAProxy using Helm as a load balancer for the PostgreSQL cluster.

### 5. Create Database and Tables
   Run the provided script to create the `movies_db` database with two related tables.

- Login to the Primary Node and Run the SQL Queries below:

kubectl exec -it <Primary-Node-Pod-Name> -n postgres -- psql -U postgres  -d postgres

- Create Database, schema and Tables:

CREATE DATABASE  movies_db;

\c movies_db

CREATE SCHEMA film:

- Create 'actors' Table

CREATE TABLE  film.actors (actor_id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, birthdate DATE);

- Create 'movies' Table with a foreign key to 'actors'

CREATE TABLE film.movies (movie_id SERIAL PRIMARY KEY, title VARCHAR(255) NOT NULL, genre VARCHAR(50), release_year INT, actor_id INT, FOREIGN KEY (actor_id) REFERENCES actors (actor_id) ON DELETE SET NULL);


### 6. Populate Data with Faker
   Execute the script to insert 100,000 records into the tables using the Faker library.

- Install Python and the required libraries:

apt update
apt install python3 python3-pip
pip3 install faker psycopg2-binary

- Create a python that can be used to run the python script:

- Create a ConfigMap from the insert.py query:

kubectl create configmap python-scripts --from-file=/home/minikubeuser/insert.py

- Create the pod from the python-deployment.yaml file:

kubectl apply -f python-deployment.yaml

- Switch to the python pod bash:

kubectl exec -it python-deployment-5768ddc7cb-jftpw -- /bin/bash

- Once switched:
run this:

python /scripts.insert.py

### 7. Set Up Async Replication
   Deploy a standalone PostgreSQL node and configure it for asynchronous replication from the primary node in the PostgreSQL cluster.

