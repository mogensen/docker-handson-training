# Working with volumes

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
## Working with volumes

Docker volumes can be used to achieve many things, including:

* Bypassing the copy-on-write system to obtain native disk I/O performance.
* Bypassing copy-on-write to leave some files out of `docker commit`.
* Sharing a directory between multiple containers.
* Sharing a directory between the host and a container.
* Sharing a *single file* between the host and a container.

---
## Volumes are special directories in a container

Volumes can be declared in two different ways.

* Within a `Dockerfile`, with a `VOLUME` instruction.

```dockerfile
VOLUME /uploads
```

* On the command-line, with the `-v` flag for `docker run`.

```bash
$ docker run -d -v /uploads myapp
```

In both cases, `/uploads` (inside the container) will be a volume.

---
## Volumes bypass the copy-on-write system

Volumes act as passthroughs to the host filesystem.

* The I/O performance on a volume is exactly the same as I/O performance
  on the Docker host.
* When you `docker commit`, the content of volumes is not brought into
  the resulting image.
* If a `RUN` instruction in a `Dockerfile` changes the content of a
  volume, those changes are not recorded neither.
* If a container is started with the `--read-only` flag, the volume
  will still be writable (unless the volume is a read-only volume).

---
## Volumes can be shared across containers

You can start a container with *exactly the same volumes* as another one.

* The new container will have the same volumes, in the same directories.
* They will contain exactly the same thing, and remain in sync.
* Under the hood, they are actually the same directories on the host anyway.
* This is done using the `--volumes-from` flag for `docker run`.

---
## Sharing app server logs with another container

Let's start a Tomcat container:

```bash
$ docker run --name webapp -d -p 8080:8080 -v /usr/local/tomcat/logs tomcat
```

Now, start an `alpine` container accessing the same volume:

```bash
$ docker run --volumes-from webapp alpine sh -c "tail -f /usr/local/tomcat/logs/*"
```

Then, from another window, send requests to our Tomcat container:
```bash
$ curl localhost:8080
```

---
## Volumes exist independently of containers

If a container is stopped, its volumes still exist and are available.

Volumes can be listed and manipulated with `docker volume` subcommands:

```bash
$ docker volume ls
DRIVER              VOLUME NAME
local               5b0b65e4316da67c2d471086640e6005ca2264f3...
local               pgdata-prod
local               pgdata-dev
local               13b59c9936d78d109d094693446e174e5480d973...
```

Some of those volume names were explicit (`pgdata-prod`, `pgdata-dev`).

The others (the hex IDs) were generated automatically by Docker.

---
## Naming volumes

* Volumes can be created without a container, then used in multiple containers.

Let's create a couple of volumes directly.

```bash
$ docker volume create webapps
webapps
```

```bash
$ docker volume create logs
logs
```

Volumes are not anchored to a specific path.

---
## Using our named volumes

* Volumes are used with the `-v` option.

* When a host path does not contain a /, it is considered to be a volume name.

Let's start a web server using the two previous volumes.

```bash
$ docker run -d -p 1234:8080 \
         -v logs:/usr/local/tomcat/logs \
         -v webapps:/usr/local/tomcat/webapps \
         tomcat
```

Check that it's running correctly:

```bash
$ curl localhost:1234
... (Tomcat tells us how happy it is to be up and running) ...
```

---
## Using a volume in another container

* We will make changes to the volume from another container.
* In this example, we will run a text editor in the other container.

  (But this could be a FTP server, a WebDAV server, a Git receiver...)

Let's start another container using the `webapps` volume.

```bash
$ docker run -v webapps:/webapps -w /webapps -ti alpine vi ROOT/index.jsp
```

Vandalize the page, save, exit.

Then run `curl localhost:1234` again to see your changes.

---
## Managing volumes explicitly

In some cases, you want a specific directory on the host to be mapped
inside the container:

* You want to manage storage and snapshots yourself.

    (With LVM, or a SAN, or ZFS, or anything else!)

* You have a separate disk with better performance (SSD) or resiliency (EBS)
  than the system disk, and you want to put important data on that disk.

* You want to share your source directory between your host (where the
  source gets edited) and the container (where it is compiled or executed).

Wait, we already met the last use-case in our example development workflow!
Nice.

```bash
$ docker run -d -v /path/on/the/host:/path/in/container image ...
```

---
## Migrating data with `--volumes-from`

The `--volumes-from` option tells Docker to re-use all the volumes
of an existing container.

* Scenario: migrating from Redis 2.8 to Redis 3.0.
* We have a container (`myredis`) running Redis 2.8.
* Stop the `myredis` container.
* Start a new container, using the Redis 3.0 image, and the `--volumes-from` option.
* The new container will inherit the data of the old one.
* Newer containers can use `--volumes-from` too.

---
## Data migration in practice

Let's create a Redis container.

```bash
$ docker run -d --name redis28 redis:2.8
```

Connect to the Redis container and set some data.

```bash
$ docker run -ti --link redis28:redis alpine telnet redis 6379
```

Issue the following commands:

```bash
SET counter 42
INFO server
SAVE
QUIT
```

---
## Upgrading Redis

Stop the Redis container.

```bash
$ docker stop redis28
```

Start the new Redis container.

```bash
$ docker run -d --name redis30 --volumes-from redis28 redis:3.0
```

---
## Testing the new Redis

Connect to the Redis container and see our data.

```bash
docker run -ti --link redis30:redis alpine telnet redis 6379
```

Issue a few commands.

```bash
GET counter
INFO server
QUIT
```

---
## Volumes lifecycle

* When you remove a container, its volumes are kept around.
* You can list them with `docker volume ls`.
* You can access them by creating a container with `docker run -v`.
* You can remove them with `docker volume rm` or `docker system prune`.

Ultimately, _you_ are the one responsible for logging,
monitoring, and backup of your volumes.

---
## Checking volumes defined by an image

Wondering if an image has volumes? Just use `docker inspect`:

```bash
$ # docker inspect training/datavol
[{
  "config": {
    . . .
    "Volumes": {
        "/var/webapp": {}
    },
    . . .
}]
```

---
## Checking volumes used by a container

To look which paths are actually volumes, and to what they are bound,
use `docker inspect` (again):

```bash
$ docker inspect <yourContainerID>
[{
  "ID": "<yourContainerID>",
. . .
  "Volumes": {
     "/var/webapp": "/var/lib/docker/vfs/dir/f4280c5b6207ed531efd4cc673ff620cef2a7980f747dbbcca001db61de04468"
  },
  "VolumesRW": {
     "/var/webapp": true
  },
}]
```

* We can see that our volume is present on the file system of the Docker host.

---
## Sharing a single file

* An interesting examples is to share the Docker control socket.

```bash
$ docker run -it -v /var/run/docker.sock:/var/run/docker.sock docker sh
```

* From that container, you can now run `docker` commands communicating with
the Docker Engine running on the host.

> Since that container has access to the Docker socket, it has root-like access to the host.

---
## Volume plugins

You can install plugins to manage volumes backed by particular storage systems,
or providing extra features. For instance:

* [dvol](https://github.com/ClusterHQ/dvol) - allows to commit/branch/rollback volumes;
* [Flocker](https://clusterhq.com/flocker/introduction/), [REX-Ray](https://github.com/emccode/rexray) - create and manage volumes backed by an enterprise storage system (e.g. SAN or NAS), or by cloud block stores (e.g. EBS);
* [Blockbridge](http://www.blockbridge.com/), [Portworx](http://portworx.com/) - provide distributed block store for containers;
* and much more!

---
## Section summary

We've learned how to:

* Create and manage volumes.
* Share volumes across containers.
* Share a host directory with one or many containers.