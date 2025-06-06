# Create a docker register

sudo docker run -d -p 5000:5000 --name registry registry:2.7



sudo kind  delete cluster --name openfaas
sudo kind create cluster --config openfaas-cluster.yaml --name openfaas
arkade install openfaas

kubectl get deployments -n openfaas -l "release=openfaas, app=openfaas"
sudo   kubectl rollout status -n openfaas deploy/gateway
sudo   kubectl port-forward -n openfaas svc/gateway 8080:8080 &

lLUTwTvJfy0K
faas-cli template pull
faas-cli template store pull python3-http

-------------------------------------------

sudo kind  delete cluster --name openfaas

sudo bash kind-with-registry.bash
sudo kubectl cluster-info --context kind-openfaas
arkade install openfaas

kubectl get deployments -n openfaas -l "release=openfaas, app=openfaas"
sudo   kubectl rollout status -n openfaas deploy/gateway
sudo   kubectl port-forward -n openfaas svc/gateway 8080:8080 &
PASSWORD=$(sudo kubectl get secret -n openfaas basic-auth -o jsonpath="{.data.basic-auth-password}" | base64 --decode; echo)


curl -X POST http://127.0.0.1:8080/function/pydict -d "run"
echo $PASSWORD | sudo faas-cli login --username admin --password-stdin

sudo faas-cli up -f stack.yaml

curl -X POST http://127.0.0.1:8080/function/pydict -d "run"
curl -X POST http://127.0.0.1:8080/function/pyecho -d "echo"
echo "advocate" | sudo faas-cli invoke pyecho


