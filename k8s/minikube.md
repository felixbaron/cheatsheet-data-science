# minikube

## Install minikube

For Windows download the [installer](https://storage.googleapis.com/minikube/releases/latest/minikube-installer.exe).

On Linux:

```shell
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

## minikube status

```shell
minikube status
```

## Start/stop minikube

```shell
minikube stop
minikube start
```

## Interact with minikube

```shell
kubectl get po -A
```

## Launch the dashboard

```shell
minikube addons enable dashboard
minikube dashboard
```

## Addons

```shell
minikube addons list
minikube addons enable addon
```

### MetalLB

```shell
minikube addons enable metallb
```
