FROM apache/spark-py

USER root
# Install additional libraries if required
RUN pip install pandas numpy matplotlib

WORKDIR /workspace
COPY workspace/kmeans.py kmeans.py

USER root
CMD ["/opt/spark/bin/spark-submit" ,"kmeans.py"]