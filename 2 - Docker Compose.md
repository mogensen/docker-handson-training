---
## Docker Compose

Defining and running multi-container Docker applications
---
##



29
Multiple container application in Docker
$ docker pull
mysql
$
docker pull
wordpress
$
docker run -d --name=db -e MYSQL_ROOT_PASSWORD=root
mysql
$
docker run --name=wp -p 8000:80 --link
db:db
-e WORDPRESS_DB_HOST=db

WORDPRESS_DB_PASSWORD=root wordpress
---
##



Docker Compose - YAML
version: '2'
services:


db:

image
: mysql

environment
:

MYSQL_ROOT_PASSWORD
: root

wp
:

depends_on
:

-
db

image
: wordpress

ports
:

-
"8000:80"

environment
:

WORDPRESS_DB_HOST
: db

WORDPRESS_DB_PASSWORD
: root
$ docker pull mysql
$ docker pull wordpress
$ docker run -d --
name=db


MYSQL_ROOT_PASSWORD=root mysql
$ docker run --
name=wp
-p 8000:80 	--
link db:db 	-e WORDPRESS_DB_HOST=db 	-e
WORDPRESS_DB_PASSWORD=root

wordpress
---
##



Docker Compose - YAML
version: '2'
services:


db:

image
: mysql

environment
:

MYSQL_ROOT_PASSWORD
: root

wp
:

depends_on
:

-
db

image
: wordpress

ports
:

-
"8000:80"

environment
:

WORDPRESS_DB_HOST
: db

WORDPRESS_DB_PASSWORD
: root
$ docker-compose
up
$ docker-compose
ps
$ docker-compose
stop
---
##



Docker Swarm
Setting up a basic docker
cluster
---
##



Docker Swarm mode
// http://play-with-docker.com
$
docker

swarm
init
--advertise-
addr

eth0
// join nodes
$
docker
swarm join ...
$
docker
node ls
---
##



The Vote Application
![image](pptimages/image10.jpeg)
---
##



Docker Swarm mode
// download stack definition
$ curl -O
https://
raw.githubusercontent.com/docker/example-voting-app/master/docker-stack.yml
// Spin up cluster
$
docker stack deploy -c docker-stack.yml vote
---
##



Getting started!
---
##



Docker on Linux
Create a
L
inux VM (or use physical), and install Docker
Requires kernel 3.10
Stable builds
curl –
sSL
https://get.docker.com/ |
sh
Test and experimental builds
curl –
sSL
https://test.docker.com/ |
sh
curl –
sSL
https://experimental.docker.com/ |
sh
Can also manually install (see docs)
---
##



Docker for Windows / Mac
Currently in public beta
Easy to install: Get up and running on Docker in minutes
Leverages Hyper-V (Windows) or
xhyv
(Mac)
Docker for Windows requires
Windows Pro 10, Enterprise, or Education
Full API / CLI compatibility
OS integration for increased stability and speed
---
##



Docker for Azure / AWS
Easily deploy Docker 1.12 Swarm clusters (Linux)
Scale up and down easily
Integrate with underlying platform (i.e. load balancers)
---
##



Docker + Windows Server = Windows Containers
Native Windows containers powered by Docker Engine
Windows kernel engineered with new primitives to support containers
Deep integration with 2+ years of engineering collaboration in Docker Engine and Windows Server
Microsoft is top 5 Docker open source project contributor and a Docker maintainer
Infrastructure
Windows Server 2016
Bins/Libs
App
Docker Engine
Bins/Libs
App
Bins/Libs
App
---
##



Walk, Jog, Run
Walk:
Setup your preferred Docker environment
Fire up some prebuilt images (
nginx
, hello-world,
mikegcoleman
/
catweb
)
Jog:
Pick a well documented solution (
W
ordpress
, Jenkins,
etc
)
Build it for yourself (blogs are your friend)
Run:
Extend one your Walk solution or
Dockerize
an existing project
Build your own
Dockerfiles
Experiment with Docker Compose and Swarm Mode
---
##



Where to go from here?
https://
github.com/docker/labs
https://prakhar.me/docker-curriculum
/
https://europe-2017.dockercon.com/
---
##



Thank You.
Questions?
---
##



