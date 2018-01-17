# Docker Compose exercises

## About this exercise set

> To help the users of this exercise to learn how to use docker and where to get help when they are stuck in the real world, I have tried to create exercises that forces the user to look in documentation and experiment.

> **This means, that the exercise set is not a simple copy & paste exercise**

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

See https://docs.docker.com/compose/compose-file/ for help.
Use version 3 or above.

### Build and start

Standing in the directory where the `docker-compose.yml` file is, we can execute the following

```shell

# Build all services that use the `build` notation
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

Follow the official Docker documentation to publish the python addition server to your docker hub account.
_Note_: Create a docker account if you do not already have one.

https://docs.docker.com/docker-cloud/builds/push-images/

Now change your `docker-compose.yml` file to use the published image instead of the locally build version.
Test that it works as expected.

### Host it online

Now it's time to expose our fantastic AaaS (Addition-as-a-service) to the world!
Go to play-with-docker.com and login with your docker login from docker hub.

Create a new instance of a server in the left hand menu. Copy and paste your `docker-compose.yml` file to the server.

Run `docker-compose up` and check that docker downloads the two images needed from docker hub, and starts the containers.

Now you should see a blue port number in the top of the dashboard. Click the port to go to the endpoint for your new hosted docker container.

__Congratulations!__ You now have a distributed, cloud native, container hosted application with all configurations needed expressed as code.
