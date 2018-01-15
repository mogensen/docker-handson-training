# Docker Compose

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
## Docker Compose

Defining and running multi-container Docker applications

---
## Multiple container application

```shell
$ docker pull mysql

$ docker pull wordpress

$ docker run -d --name=db -e MYSQL_ROOT_PASSWORD=root mysql

$ docker run --name=wp -p 8000:80 --link db:db \
	-e WORDPRESS_DB_HOST=db \
	-e WORDPRESS_DB_PASSWORD=root wordpress
```

@[1](Pull mysql container)
@[3](Pull wordpress container)
@[5](Start mysql container named `db` with root password)
@[7-9](Start wordpress container linked with `db` container)

---
## Docker Compose - YAML

```yaml
version: '3'
  services:
    db:
      image: mysql
      environment:
        MYSQL_ROOT_PASSWORD: root
    wp:
      depends_on:
        - db
      image: wordpress
      ports:
        - "8000:80"
      environment:
        WORDPRESS_DB_HOST: db
        WORDPRESS_DB_PASSWORD: root
```

@[2](Define all services for application)
@[3-6](Define mysql container named `db`)
@[7-15](Define wordpress container named `wp`)
@[8-9](depends_on will not wait for `db` to be "ready" before starting `wp`)

---
## Docker Compose - YAML

```yaml
version: '2'
services:
  db:
   image: mysql
   environment:
    MYSQL_ROOT_PASSWORD: root
  wp:
   depends_on:
    - db
   image: wordpress
   ports:
    - "8000:80"
   environment:
    WORDPRESS_DB_HOST: db
    WORDPRESS_DB_PASSWORD: root
```

```shell
$ docker-compose up
$ docker-compose ps
$ docker-compose stop
```

---
## Hands On

#### Exercises [here](https://github.com/mogensen/docker-handson-training/tree/master/2-Docker-compose/Exercises.md)
