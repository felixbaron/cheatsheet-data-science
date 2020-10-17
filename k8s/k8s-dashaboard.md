# Kubernetes Dashboard

## Install the dashboard;

Find the latest manifest file on [GitHub](https://github.com/kubernetes/dashboard#install)

```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.4/aio/deploy/recommended.yaml
```

## Forward the traffic

```shell
kubectl proxy
```

## Create a user

```shell
kubectl apply -f ./manifests/create-user.yml
```

## Create cluster role binding

```shell
kubectl apply -f ./manifests/create-cluster-role-binding.yml
```

## Get Bearer Token

```shell
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}')
```

```powershell
kubectl -n kubernetes-dashboard describe secret $(kubectl -n kubernetes-dashboard get secret | sls admin-user | ForEach-Object { $_ -Split '\s+' } | Select -First 1)
```

## Open dashboard

```powershell
start 'http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/'
```
