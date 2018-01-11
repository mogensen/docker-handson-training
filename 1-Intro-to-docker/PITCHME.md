# Introduction to Docker

![image](pptimages/image3.png)

---
## About me
### Frederik Mogensen

Software Pilot at Trifork
Focus on Docker, orchestration and ci/cd

![image](pptimages/image10.jpeg)
![image](pptimages/image11.png)

---
## Agenda

- Containers are NOT VMs
- Working with Docker (Build, Ship, Run)
- Container Architecture
- But Why?
- Multi-container applications

Docker Compose
Docker Swarm
Getting started
Q & A

---
# Containers are not VMs

---
## Containers are NOT VMs
Easy connection to make
Fundamentally different architectures
Fundamentally different benefits

---
## VMs
![image](pptimages/image12.png)
---
## Containers

![image](pptimages/image13.png)

---
## They’re different, not mutually exclusive

![image](pptimages/image14.png)

---
## Build, Ship, and Run

---
## Some Docker vocabulary

| ![image](pptimages/image17.png) | Docker Image       The basis of a Docker container. Represents a full application |
| ![image](pptimages/image18.png) | Docker Container   The standard unit in which the application service resides and executes |
| ![image](pptimages/image19.png) | Docker Engine      Creates, ships and runs Docker containers deployable on a physical or virtual, host locally, in a datacenter or cloud service provider |
| ![image](pptimages/image20.png) | Registry Service (Docker Hub or Docker Trusted Registry) Cloud or server based storage and distribution service for your images |

---
## Basic Docker Commands

```shell
$ docker pull mikegcoleman/catweb:latest
$ docker images
$ docker run -d -p 5000:5000 --name catweb mikegcoleman/catweb:latest
$ docker ps
$ docker stop catweb // or <container id>
$ docker rm catweb // or <container id>
$ docker rmi mikegcoleman/catweb:latest // or <image id>
```

---
## Dockerfile – Linux Example

![image](pptimages/image21.png)

- Instructions on how to build a Docker image
- Looks very similar to "native" commands
- Important to optimize your Dockerfile

---
## Basic Docker Commands

```shell
$docker build –t mikegcoleman/catweb:2.0 .
$docker push mikegcoleman/catweb:2.0
```
![image](pptimages/image21.png)


---
## Put it all together: Build, Ship, Run Workflow

![image](pptimages/diagram.png)

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
$ docker run –d –p 5000:5000 --name catweb mikegcoleman/catweb
```

Browse to port 5000 on your machine: http://localhost:5000

---
## Docker Container Architecture

---
## Image Layers

![image](pptimages/catweb-layers.PNG)

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

<!--
---
# But, Why?

---
## Enterprises are looking to Docker for critical transformations

80%
Docker is central to cloud strategy
Docker Survey: State of App development :  Q1 - 2016
3 out 4
Top initiatives revolve around applications
44%
Looking to adopt DevOps


App Modernization
DevOps
Cloud
State of App development Survey:  Q1 2016

---
## Docker delivers speed, flexibility and savings

- Agility
Portability
Control
State of App development Survey:  Q1 2016, Cornell University case study
13X
More software releases
62%
Report reduction in MTTR
10X
Cost reduction in maintaining existing applications
Eliminate
“works on my machine” issues
41%
Move workloads across private/public clouds
65%
Reduction in developer onboarding time
-->

---
## One platform delivers one journey for all applications
1 Containerize Legacy Applications
  - Lift and shift for portability and efficiency

2 Transform Legacy to Microservices
  - Look for shared services to transform

3 Accelerate New Applications
  - Greenfield innovation

---
## Containers in production with Docker Datacenter

![image](pptimages/ucp.PNG)

- Enterprise container orchestration, management and security for dev and ops
- Available today for Linux environments
- Q4 2016 beta for Windows environments 

