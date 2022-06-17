
### Astronomer airflow installation on ubuntu

#### Prerequisites:
To use the Astro CLI, make sure you have Docker (v18.09 or higher) installed and running on your machine.

#### Step 1: Install or Upgrade the Astro CLI
* Install or Upgrade the CLI via cURL
``` bash
curl -ssl https://install.astronomer.io | sudo bash
```	
*  Install or Upgrade the CLI via Homebrew
``` bash
brew install astronomer/tap/astro
```
#### Step 2: Initialize an Airflow Project
```bash
mkdir <directory-name> && cd <directory-name>
```
##### In the project directory, run:
```bash
astro dev init
```
#### Step 3: Add Airflow 2.0 to your Dockerfile

##### Note: In your Dockerfile, replace the existing FROM statement with:
* FROM  quay.io/astronomer/ap-airflow:2.0.0-2-buster-onbuild
Run this
```bash
docker pull quay.io/astronomer/ap-airflow:2.0.0-2-buster-onbuild
```
#### Step 4: Start Airflow
```bash
astro dev start
```
#### Step 5: Access the Airflow 2.0 UI
To check out the Airflow 2.0 UI:
* Go to [astro_aorflow](http://localhost:8080/astro_airflow)
* Log in with “admin” as both your username and password


### Troubleshooting:
#### Error:
```bash 
error building, (re)creating or starting project
containers: Error response from daemon: driver 
failed programming external connectivity on
endpoint airflow_2f0958-postgres-1 
(c9d1156df61529f393751f3d9f2fa17fa6ff232d22e45be9b79e31f11c26e29a):
Error starting userland proxy: listen tcp4 0.0.0.0:5432:
bind: address already in use
```
#### Solution:
- Step 1 : 
```bash
lsof -i :5432<port>  or sudo lsof -i :5432<port>
```

- Step 2 : Then it delete PID : 
```bash
kill -9 1442<PID> 
```
- Step 3: 
```bash
lsof -i :5432<port>  or sudo lsof -i :5432<port>
```
- Strep 4 : 
```bash
astro dev start
```

### To remove example Dags
 * go to your airflow >> dags folder and delete predefined python files 
 * Restart airflow webserver

### To add test dags:
* download test dag fiel from here [test_dag ](https://github.com/atul8122000/astronomer_airflow/blob/dev/test_dag.py)
* and paste in airflow >> dags folder
