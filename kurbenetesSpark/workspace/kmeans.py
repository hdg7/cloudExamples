#This program is a simple implementation of the k-means algorithm through Spark.

from pyspark import SparkContext

sc = SparkContext('local')
from pyspark.ml.clustering import KMeans

from pyspark.ml.linalg import Vectors

from pyspark.sql import SparkSession

spark = SparkSession(sc)

# Sample data (replace with your data)
#data = [(0, Vectors.dense([0.0, 0.0])), (1, Vectors.dense([0.1, 0.1])),
#        (2, Vectors.dense([0.2, 0.2])), (3, Vectors.dense([9.0, 9.0])),
#        (4, Vectors.dense([9.1, 9.1])), (5, Vectors.dense([9.2, 9.2]))]

# We create a large dataset to test the algorithm using three Gaussian distribution
from numpy import random

data = []
instances = 1000000
for i in range(instances):
    data.append((i, Vectors.dense([random.normal(0, 1), random.normal(0, 1)])))
    data.append((i + instances, Vectors.dense([random.normal(5, 1), random.normal(5, 1)])))
    data.append((i + 2*instances, Vectors.dense([random.normal(10, 1), random.normal(10, 1)])))



df = spark.createDataFrame(data, ["id", "features"])

# Create k-means model

kmeans = KMeans(k=10, seed=1)

model = kmeans.fit(df)

# Print the center of each cluster

centers = model.clusterCenters()

for center in centers:
    print(center)

