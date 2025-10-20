# Pokeberries Statistics API
This project provides a **RESTful API** and a simple **HTML view** for analyzing Pokémon berries growth-time statistics using data from the [PokeAPI](https://pokeapi.co/).

It was developed with **FastAPI**, supports **Redis caching**, and can be run both locally and via Docker.
## Run with Docker
The project is containerized using **Docker Compose**, including both the FastAPI app and Redis for caching.

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Create your environment file
Before running the containers, you must create your **.env** file using the provided template: **env.template**
### Build and Start the Services
Run the following command in the project root directory (where your `docker-compose.yml` is located):

```bash
docker compose up --build
```
## API Documentation

The project includes automatically generated interactive API documentation thanks to **FastAPI** and **OpenAPI**.

You can access it directly from the deployed version:

- **Swagger**  
[https://pokeberries-api-restless-dew-4199.fly.dev/docs](https://pokeberries-api-restless-dew-4199.fly.dev/docs)

Documentation pages are automatically generated from the FastAPI route definitions and docstrings.


## Live Demo
This API is currently deployed on **[Fly.io](https://fly.io/)** 

- **API endpoint (JSON):**  
  [https://pokeberries-api-restless-dew-4199.fly.dev/api/v1/allBerryStats](https://pokeberries-api-restless-dew-4199.fly.dev/api/v1/allBerryStats)

- **HTML view (human-readable):**  
  [https://pokeberries-api-restless-dew-4199.fly.dev/api/v1/allBerryStats/view](https://pokeberries-api-restless-dew-4199.fly.dev/api/v1/allBerryStats/view)

