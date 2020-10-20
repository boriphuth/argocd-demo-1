# argocd-demo

ArgoDC Demo

## VouTube List

<https://www.youtube.com/playlist?list=PL34sAs7_26wMW4bWKnMIfEd87aPuw75by>

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f argocd-install.yaml

kubectl -n argocd get all
kubectl -n argocd edit svc argocd-server ## change to type: NodePort

kubectl get node -o wide

kubectl scale deploy nginx --replicas 2 ## manual scale
kubectl get all
```

## [ Kube 85.3 ] Argo CD Continuous Deployment from Helm Repo

```bash
helm repo add stable https://kubernetes-charts.storage.googleapis.com/
helm repo list
```

## [ Kube 85.4 ] Argo CD Creating app using custom resource definition

```bash
kubectl get node -o wide
kubectl get all
kubectl get crds
kubectl -n argocd get applications
kubectl -n argocd get appprojects
kubectl -n argocd describe applications default

kubectl create -f argocd-demo.yaml
```