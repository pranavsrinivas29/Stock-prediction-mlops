# Airflow
```bash
export AIRFLOW_HOME=$(pwd)/airflow

airflow db init

airflow users create \
  --username admin \
  --password admin \
  --firstname Pranav \
  --lastname Srinivas \
  --role Admin \
  --email admin@example.com

airflow webserver # Terminal 1, same terminal where airflow home was set

airflow scheduler # Terminal 2

pkill -f airflow # To kill everything related to airflow

```