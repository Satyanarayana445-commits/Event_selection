# Introduction

TODO: Give a short introduction of your project. Let this section explain the objectives or the motivation behind this project.

# Vertual Environment Activation and Deactivation Command

- Activate the virtual env:

        source event_env/bin/activate

- Deactivate and Activate virtual environment

        deactivate
        source event_env/bin/activate

## Postgres Setup (Docker)

- Install Docker (if not already installed):

        curl -fsSL https://get.docker.com -o get-docker.sh
        sudo sh get-docker.sh

- Pull the Postgres image:

        sudo docker pull postgres:13

- To list the image files in system:

        sudo docker images

- You should be able to see the postgres13 image

- Navigate to the Event_project directory and create a directory for the Postgres DB:

        mkdir db_data

- From the same Event_project directory, run the Postgres Docker:

        sudo docker run --name event_db -e POSTGRES_PASSWORD='event@123' -v "$PWD"/postgres_data/:/var/lib/postgresql/data -p 5432:5432 postgres:13

  - If successful, you will get the log "database system is ready to accept connections" in terminal

- While the container is active, open a new terminal and enter:

        sudo docker exec -it event_db bash

  - This will open a bash instance in the postgres container

- Enter the following commands to create user and DB:

        psql -U postgres
        CREATE USER event_user WITH PASSWORD 'Event' CREATEDB;
        CREATE DATABASE event OWNER event_user;

- Check the list of DB to verify that event DB has been created with owner event_user:

          \l
-
    \c binpick

- To quit psql:

        \q

- To exit postgres container:

        exit

- Open a new terminal and run "create_db_tables.py' to create all the required DataBase tables.

        python3 create_db_tables.py




