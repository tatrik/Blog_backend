# Blog_backend

This repository shows how to use Fastapi with databases and Alembic to work asynchronously with databases.

This project implements:
 - authorization using jwt and OAuth2
 - data validation using pydantic
 - Password storage and validation using hashing. Passwords are not stored in raw form.
 - CRUD for users and posts
 - asynchronous database operation
 - creating and using migrations in databases using Alembic
 - using .env file to store and pass environment variables
 - application containerization using Docker and Docker-compose
 - using volumes to save data from the database


## How to build

	make build

## How to crate tables in db

	make migrations

## How to run

	make up

and go to:

[http://localhost:8000/docs](http://localhost:8000/docs)

## How to stop and destroy

	make down