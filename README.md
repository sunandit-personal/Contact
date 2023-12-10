## Install Postgres For Database
Link : https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04

## Database Config
1. Create user with password.
2. Create a database with owner that user.
3. grant all privileges on the db to the owner.
## Command
1. Going to psql command prompt
```
sudo -u postgres psql
```
2. Run postgres command
```
postgres=# CREATE USER "your_database_user" WITH PASSWORD 'your_desired_password';
CREATE ROLE
postgres=# CREATE DATABASE "db_name" OWNER "databse_user";
CREATE DATABASE
postgres=# GRANT ALL PRIVILEGES ON DATABASE "dcontact_dbatabase_name" TO db_user;
GRANT
postgres=# \q

```

## Install Virtualenv
1. Install Python3-pip
2. Install virtualenv via pip3
3. Activate the virtual env

## Build new virtualenv
```
virtualenv -p python3.8 "your env name"
```
## Activate
```
source  ~/<your env name>/bin/activate
```
## Run requirements.txt
Run this file to install the project dependency on your virtualenv.

```
pip install -r requirements.txt
```

## Database migrate
```
python manage.py migrate
```
## Run the server
```
python manage.py runserver
```

## For testcase run this command
```
python manage.py test contact
```
