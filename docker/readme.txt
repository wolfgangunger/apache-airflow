https://airflow.apache.org/docs/apache-airflow/stable/index.html

https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

http://www.marknagelberg.com/getting-started-with-airflow-using-docker/

AWS Dags:
https://github.com/apache/airflow/tree/main/airflow/providers/amazon/aws/example_dags


sudo chmod u=rwx,g=rwx,o=rwx ./logs

docker-compose up airflow-init

docker-compose up

--
docker ps

docker exec -ti <container name> bash

--

docker-compose down --volumes --remove-orphans
