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

## [ Kube 85.6 ] Getting started with Argo CD CLI

```bash
curl -LO https://github.com/argoproj/argo-cd/releases/download/v1.7.8/argocd-darwin-amd64
mv argocd-darwin-amd64 argocd
chmod +x argocd
sudo mv argocd /usr/local/bin
which argocd
argocd help

kubectl get node -o wide
kubectl  -n argocd get all

argocd login 192.168.99.102:32494
argocd login 192.168.99.102:32494 --insecure
admin
argocd-server-6bcbf7997d-92tgk

argocd cluster list
argocd proj list
argocd repo list
argocd app list
argocd logout 192.168.99.102:32494

argocd login 192.168.99.102:32494 --insecure --username admin --password argocd-server-6bcbf7997d-92tgk

argocd proj create myproj
argocd account get-user-info
argocd account update-password
argocd login 192.168.99.102:32494 --insecure --username admin --password admin
argocd app list
argocd app create argocd-demo --repo https://github.com/boriphuth/argocd-demo-1 --path yamls --dest-namespace default --dest-server https://kubernetes.default.svc
argocd app sync argocd-demo
argocd app resources argocd-demo
argocd app delete argocd-demo
```

az storage container list --connection-string 'DefaultEndpointsProtocol=https;AccountName=sccvmsafb5881caded8c178;AccountKey=3Cr/OyCY4QTY/rbmrNjm9qgzzXVXsN3/7hZtdncaVmBmX25Sw58hnA0UoA1ELKBv4GhL26jo7J6/NDBw/CP+Kg==;EndpointSuffix=core.windows.net'

scout azure --user-account --username velma.vanderduck@scctraining332.onmicrosoft.com --password 'SecurePassword9182' --force --no-browser

"appId": "00000003-0000-0ff1-ce00-000000000000"