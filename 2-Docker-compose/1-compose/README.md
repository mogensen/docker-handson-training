# Docker Compose exercises

A web application for adding numbers with a centralized hitcounter.

## Files

### `addition-server/addition.py`

Python server that adds two numbers and uses redis as a centralized statistics cache.

## Exercise

### Create `Dockerfile`

First create a dockerfile in the `addition-server` directory that describes how to build an image capable of running the python application.

### Create `docker-compose.yml`

Add two services in the `docker-compose.yml` file to run:

 - redis cache in version 3
 - the python addition server image.

### Build and start

Standing in the directory where the `docker-compose.yml` file is, we can execute the following

```shell
## Build all services that use the `build` notation
$ docker-compose build
# Start all services that are described in the `docker-compose.yml` file
$ docker-compose up
```

Now you should be able to access the following:

- http://localhost:5000/add?A=2&B=32
- http://localhost:5000/stats

### Cleanup

```shell
## Build all services that use the `build` notation
$ docker-compose stop
# Start all services that are described in the `docker-compose.yml` file
$ docker-compose rm
```

### Playing around

Try to start the docker compose stack and hitting the add endpoint. See that the counter goes up.
Now try to stop the stack without running `rm`. Start the stack again and see how this effected the counter.

Now try stopping and removing the stack. Start it agin and observe the counter.

### Publishing to a Docker repository


