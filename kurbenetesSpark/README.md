# Kubernetes and Spark

This is an example of scaling Spark K-means with Kubernetes

## Steps

Create the Docker machine and run it with a single GPU:

```
sudo docker build . -t kmeans
sudo docker run -it --cpus=1 kmeans
```

This should run for 5 minutes in a machine with the appropriate resources.

Now we will use Kubernetes.

Create a cluster with kind.

```
sudo kind create cluster --name mycluster --config kind.config.yaml
```

Load your Spark image to the cluster

```
sudo kind load docker-image kmeans --name mycluster
```

Upload the Spark configuration for the different workers:

```
sudo kubectl apply -f spark.yaml
```

Run the JobL

```
sudo kubectl apply -f spark.job.yaml
```

Monitor the jod with:
```
sudo kubectl describe job my-spark-job
```

Once it finishes, check the results:
```
sudo kubectl logs job/my-spark-job
```

To kill the cluster:
```
sudo kind delete cluster --name mycluster
```

## For Monitoring

If you need to monitor the pods, deploys, jobs use:
```
sudo kubectl get pod
sudo kubectl get jobs
sudo kubectl get deploy
```

To remove pod, deploys or jobs, use:
```
sudo kubectl delete deploy spark-worker
sudo kubectl delete job my-spark-job
```