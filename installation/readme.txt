# Airflow needs a home. `~/airflow` is the default, but you can put it
# somewhere else if you prefer (optional)
#export AIRFLOW_HOME=~/airflow
set AIRFLOW_HOME=C:\workspaces\aws\MWAA\installation

# Install Airflow using the constraints file
set AIRFLOW_VERSION=2.2.0
#set PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
set PYTHON_VERSION=3.9.1

# For example: 3.6
set CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.2.0/constraints-3.9.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.2.0/constraints-3.6.txt
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
pip install "apache-airflow2.2.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.0/constraints-3.9.txt"

# The Standalone command will initialise the database, make a user,
# and start all components for you.
airflow standalone

# Visit localhost:8080 in the browser and use the admin account details
# shown on the terminal to login.
# Enable the example_bash_operator dag in the home page