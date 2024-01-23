# A Mars Rover camera viewer

## Getting Started
Dependencies:
* Docker - See [Get Docker](https://docs.docker.com/get-docker/)
* Docker Compose - Installed with Docker Desktop, See [Install Docker Compose](https://docs.docker.com/compose/install/)

With the dependencies installed, running the project is as simple as running:
```bash
docker compose up
```

This will pull the required Docker images and spin up a container running your service on http://localhost:8000.

To end the service, press `Ctrl+C`


Welcome to the documentation for A Mars Rover camera viewer. This API provides access to Mars photos captured by the Curiosity rover on different Earth dates.

## API Endpoint

The base URL for the API is: `http://localhost:8000/api/v1/`

### Get Mars Photos for a Specific Earth Date

Endpoint: `GET /api/v1/mars-photos/{earth_date}/`

Retrieve Mars photos for a specific Earth date.

#### Parameters

- `earth_date` (str): The Earth date in the format 'YYYY-MM-DD'.

#### Example

```bash
curl http://localhost:8000/api/v1/mars-photos/2015-12-23/
