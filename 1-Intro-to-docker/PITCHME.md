# Introduction to Docker

---
## About me
### Frederik Mogensen

<div class="left-col-big">
Software Pilot at Trifork
<br>
<i>Focus on Docker, orchestration and ci/cd</i>
</div>
<div class="right-col-small">
![image](assets/images/me.jpeg)
</div>

---
# Containers are not VMs

---
## Containers are NOT VMs

- Easy connection to make
- Fundamentally different architectures
- Fundamentally different benefits

---
## VMs

![image](assets/images/image12.png)

---
## Containers

![image](assets/images/image13.png)

---
## They’re different, not mutually exclusive

![image](assets/images/image14.png)


---
# Build, Ship, and Run

---
## Docker vocabulary

- Docker Image
  - The basis of a Docker container. Represents a full application.
- Docker Container 
  - The standard executing unit
- Docker Engine 
  - Creates, ships and runs Docker containers
- Registry Service
  - Cloud or server based storage and distribution of images

![image](assets/images/image18.png)
![image](assets/images/image17.png)
![image](assets/images/image19.png)
![image](assets/images/image20.png)

---
## Basic Docker Commands

```bash
docker pull mikegcoleman/catweb:latest
docker images
docker run -d -p 5000:5000 --name catweb mikegcoleman/catweb:latest
docker ps
docker stop catweb // or <container id>
docker rm catweb // or <container id>
docker rmi mikegcoleman/catweb:latest // or <image id>
```

---
## Dockerfile – Linux Example

- Instructions on how to build a Docker image
- Looks very similar to "native" commands

```dockerfile
FROM alpine:latest

RUN apk add --update py-pip

RUN pip install --upgrade pip

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/

EXPOSE 5000

CMD ["python", "/usr/src/app/app.py"]
```

@[1](Our base image)
@[3](Install python and pip)
@[5](Upgrade pip)
@[7-8](Install Python modules needed by the Python app)
@[10-11](Copy files required for the app to run)
@[13](Tell the port number the container should expose)
@[15](How should docker start the application)

---
## Basic Docker Commands

```dockerfile
FROM alpine:latest
RUN apk add --update py-pip
RUN pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY app.py /usr/src/app/
COPY templates/index.html /usr/src/app/templates/
EXPOSE 5000
CMD ["python", "/usr/src/app/app.py"]
```

```shell
docker build –t mikegcoleman/catweb:2.0 .
docker push mikegcoleman/catweb:2.0
```

---
## Put it all together

![image](assets/images/diagram.png)

---
## Demo

Build, Ship, and Run

---
## Now you try it!

- Visit http://docs.docker.com/installation
- Install the right version of Docker for your machine
- Docker for Mac
- Docker for Windows
- After Docker is installed, run Catweb

```shell
$ docker run –p 5000:5000 --name catweb mikegcoleman/catweb
```

Browse to port 5000 on your machine: http://localhost:5000

---
# Background containers

---

## Objectives

Our first containers were *interactive*.

We will now see how to:

* Run a non-interactive container.
* Run a container in the background.
* List running containers.
* Check the logs of a container.
* Stop a container.
* List stopped containers.

---

## A non-interactive container

We will run a small custom container.

This container just displays the time every second.

```bash
$ docker run jpetazzo/clock
Fri Feb 20 00:28:53 UTC 2015
Fri Feb 20 00:28:54 UTC 2015
Fri Feb 20 00:28:55 UTC 2015
...
```

* This container will run forever.
* To stop it, press `^C`.

Note:

* Docker has automatically downloaded the image `jpetazzo/clock`.
* This image is a user image, created by `jpetazzo`.
* We will hear more about user images (and other types of images) later.

---

## Run a container in the background

Containers can be started in the background, with the `-d` flag (daemon mode):

```bash
$ docker run -d jpetazzo/clock
47d677dcfba4277c6cc68fcaa51f932b544cab1a187c853b7d0caf4e8debe5ad
```

* We don't see the output of the container.
* But don't worry: Docker collects that output and logs it!
* Docker gives us the ID of the container.

---

## List running containers

How can we check that our container is still running?

With `docker ps`, just like the UNIX `ps` command, lists running processes.

```bash
$ docker ps
CONTAINER ID  IMAGE           ...  CREATED        STATUS        ...
47d677dcfba4  jpetazzo/clock  ...  2 minutes ago  Up 2 minutes  ...
```

Note:

Docker tells us:

* The (truncated) ID of our container.
* The image used to start the container.
* That our container has been running (`Up`) for a couple of minutes.
* Other information (COMMAND, PORTS, NAMES) that we will explain later.

---

## Starting more containers

Let's start two more containers.

```bash
$ docker run -d jpetazzo/clock
57ad9bdfc06bb4407c47220cf59ce21585dce9a1298d7a67488359aeaea8ae2a
```

```bash
$ docker run -d jpetazzo/clock
068cc994ffd0190bbe025ba74e4c0771a5d8f14734af772ddee8dc1aaf20567d
```

Check that `docker ps` correctly reports all 3 containers.

---
## View the logs of a container

Docker collects all logs from the containers output.

Let's see that now.

```bash
$ docker logs 068
Fri Feb 20 00:39:52 UTC 2015
Fri Feb 20 00:39:53 UTC 2015
...
```

Note:
* We specified a *prefix* of the full container ID.
* You can, of course, specify the full ID.
* The `logs` command will output the *entire* logs of the container.

---
## View only the tail of the logs

To avoid being spammed with eleventy pages of output,
we can use the `--tail` option:

```bash
$ docker logs --tail 3 068
Fri Feb 20 00:55:35 UTC 2015
Fri Feb 20 00:55:36 UTC 2015
Fri Feb 20 00:55:37 UTC 2015
```

Note:

* The parameter is the number of lines that we want to see.

---

## Follow the logs in real time

Just like with the standard UNIX command `tail -f`, we can
follow the logs of our container:

```bash
$ docker logs --tail 1 --follow 068
Fri Feb 20 00:57:12 UTC 2015
Fri Feb 20 00:57:13 UTC 2015
^C
```

* This will display the last line in the log file.
* Then, it will continue to display the logs in real time.
* Use `^C` to exit.

---
## Docker Container Architecture

---
## Image Layers

![image](assets/images/catweb-layers.png)

---
## Docker File System

- Logical file system by grouping different file system primitives into branches (directories, file systems, subvolumes, snapshots)

- Each branch represents a layer in a Docker image

- Allows images to be constructed / deconstructed as needed vs. a huge monolithic image (ala traditional virtual machines)

- When a container is started a writeable layer is added to the “top” of the file system

---
## Copy on Write

- Super efficient:
  - Sub second instantiation times for containers
  - New container can take &lt;1 Mb of space

- Containers appears to be a copy of the original image
- But, it is really just a link to the original shared image

- If someone writes a change to the file system, a copy of the affected file/directory is "copied up"

---
## What about data persistence?

- Volumes allow you to specify a directory in the container that exists outside of the
docker file system structure
- Can be used to share (and persist) data between containers

- Directory persists after the container is deleted
  - Unless you explicitly delete it

- Can be created in a Dockerfile or via CLI

---
## One platform - one journey
___For all applications___

1. Containerize Legacy Applications
   - Lift and shift for portability and efficiency
1. Transform Legacy to Microservices
   - Look for shared services to transform
1. Accelerate New Applications
   - Greenfield innovation

---
## Docker Datacenter
_Containers in production_

![image](assets/images/ucp.png)

Note:
- Enterprise container orchestration, management and security for dev and ops
- Available today for Linux environments
- Q4 2016 beta for Windows environments 


---
## Hands On

#### Playing with docker containers

#### Exercises [here](https://github.com/mogensen/docker-handson-training/tree/master/1-Intro-to-docker/1-running-containers)

---
## Building images

---
## Docker Cheat Sheet

Building

```shell
$ docker build -t my-image .
$ docker build -t my-image -f my.dockerfile .
```

Running

```shell
$ docker run my-image
$ docker run -p 9000:8080 --name my-container my-image
```

Cleanup

```shell
$ docker stop my-container // Or container id from docker ps
$ docker rm my-container   // Or container id from docker ps
```

---
## Hands On

#### Creating images

#### Exercises [here](https://github.com/mogensen/docker-handson-training/tree/master/1-Intro-to-docker/2-building-images)

---
## Docker Stop

Did you notice that the `docker-compose stop` took a long time for the python app?

---
## `docker stop`
_And also `docker-compose stop`_

> The main process inside the container will receive `SIGTERM`, and after a grace period, `SIGKILL`.


---
### `addition.py`

`web.py` does not handle `SIGTERM` out of the box.

- Docker sends the `SIGTERM` signal
- the container doesn't react to this signal
- 10 seconds later, since the container is still running, Docker sends the `SIGKILL` signal
- this terminates the container
