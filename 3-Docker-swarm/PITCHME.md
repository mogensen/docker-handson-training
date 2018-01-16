# Container Orchestration with Docker Swarm

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
# Running `N` containers on `M` machines ?

---
## Independent Docker hosts

- Deployment on M machines ?
- Updating N containers ?
- Scheduling N on M ?
- Possible solutions
  - Chef
  - Puppet
  - Ansible

---
## Containers manually allocated on multiple nodes

- Non-linear resources usage
- No service discovery, hardcoded configurations
- Manual reaction to failures

- Possible solutions 
  - Manually monitor nodes and reschedule containers
  - Maintain list of services on nodes

---
## Storage for containers

- Store on node?
- Manually integrate to network storage

---
## Pets VS Cattle



![image](assets/images/cattle_no_text.png)


|    |    |
| -- | -- |
| - Unique systems that can never be down, build and managed manually | ” When one of them gets sick, you shoot 'em in the head and replace 'em with a new one.”  |

<small>https://www.slideshare.net/zhurbilo/artem-zhurbilo-some-ways-to-set-up-the-server-highload-strategy-meetup</small>

---
## The Monolith Retirement
![image](assets/images/monolithcomic.png)

<small>http://turnoff.us/geek/monolith-retirement/</small>

---
# Orchestration

---
## What is Container Orchestration


<div class="left-col">
  <ul>
    <li>Cluster management</li>
    <li>Scaling</li>
    <li>Service discovery</li>
    <li>Load balancing</li>
    <li>Networking</li>
    <li>Security</li>
  </ul>
</div>
<div class="right-col">
  <ul>
    <li>Rolling updates</li>
    <li>Storage</li>
    <li>Configuration</li>
    <li>Secrets</li>
    <li>…</li>
  </ul>
</div>

---
## What is Container Orchestration

![image](assets/images/swarm.jpg)
![image](assets/images/kubernetes.jpg)
![image](assets/images/mesos.jpg)

---
## Desired state

![image](assets/images/desired_state.png)

<small>https://www.slideshare.net/Docker/container-orchestration-from-theory-to-practice</small>

---
## Scaling Services

<div class="clearfix">
<div class="left-col">
  <ul>
    <li>Declare the number of services</li>
    <li>Scale up or down</li>
  </ul>
</div>
<div class="right-col">
![image](assets/images/microservice_architecture.png)
</div>
</div>

<small>https://martinfowler.com/articles/microservices.html</small>

---
## Service Discovery

<div class="clearfix">
<div class="left-col">
  <ul>
    <li>Allow for services in the cluster to locate other services
    <ul>
      <li>DNS</li>
      <li>API</li>
      <li>Load balancing
      <ul>
        <li>Running containers</li>
        <li>Not dead containers</li>
      </ul>
      </li>
      </ul>
    </li>
  </ul>
</div>
<div class="right-col">
![image](assets/images/microservice_architecture.png)
</div>
</div>

<small>https://martinfowler.com/articles/microservices.html</small>

---
## Load Balancing

- Expose services to external users
- Distribution of workloads across multiple computing resources
- Optimize resource usage
- Maximize throughput
- Avoid overload of any single resource
- Increase reliability and availability through redundancy

---
# Docker Swarm

---
## Core concepts

<div class="clearfix">
  <div class="left-col">
    <ul>
      <li>Swarm</li>
      <li>Node</li>
      <li>Service</li>
      <li>Tasks</li>
      <li>Secrets</li>
    </ul>
  </div>
  <div class="right-col">

![image](assets/images/swarm.png)

  </div>
</div>

---
## How nodes work

![image](assets/images/swarm_architecture.png)

<small>https://docs.docker.com/engine/swarm</small>

---
## How services work

<div class="clearfix">
  <div class="left-col">

  <ul>
    <li>In a service we specify
    <ul>
      <li>Image</li>
      <li>Exposing external ports</li>
      <li>Overlay network for connecting to other services</li>
      <li>CPU and memory limits and reservations</li>
      <li>Update policy</li>
      <li>Number of replicas</li>
    </ul>
    </li>
  </ul> 

  </div>
  <div class="right-col">

![image](assets/images/swarm_service.png)

  </div>
</div>

<small>https://docs.docker.com/engine/swarm</small>

---
## Services modes

<div class="clearfix">
  <div class="left-col">
  <ul>
    <li>Replicated
      <ul>
        <li>Specify the number of identical tasks you want</li>
      </ul>
    </li>
    <li>Global services
      <ul>
        <li>Service that runs one task on every node</li>
      </ul>
    </li>
  </ul>

  </div>
  <div class="right-col">

![image](assets/images/swarm_service_mode.png)

  </div>
</div>

<small>https://docs.docker.com/engine/swarm</small>

---
## Configuration

#### Environment variables

```yaml
  web:
    environment:
      - DEBUG
```
#### Environment files

```yaml
  web:
    env_file:
      - web-variables.env
```

---
## Networks

<div class="left-col">
Developer-edition

![image](assets/images/swarm_network_simple.png)
</div>
<div class="right-col">
Network-guy-edition

![image](assets/images/swarm_network_advanced.png)
</div>

<small>http://blog.nigelpoulton.com/demystifying-docker-overlay-networking/</small>

---
## Secrets

```shell
$ echo "This is a secret" \
  | docker secret create my_secret –

$ docker service create --name redis \
  --secret my_secret redis:alpine

$ docker exec redis \
  cat /run/secrets/my_secret

This is a secret
```

---
## Secrets

![image](assets/images/swarm_secrets.png)

<small>https://blog.docker.com/2017/02/docker-secrets-management/</small>

---
## Docker Swarm Cheat Sheet

Swarm

```shell
$ docker swarm init --advertise-addr $IP/$NET_INTERFACE
$ docker swarm join --token SWMTKN-1-49n… $MANAGER_IP:2377
$ docker swarm leave
```

Node

```shell
$ docker node ls
$ docker node update --availability drain $NODE_ID
$ docker node update --availability active $NODE_ID
$ docker node promote $NODE_ID
```

---
## Docker Swarm Cheat Sheet

Services

```shell
$ docker service create --name=$SERVICE_ID $IMAGE
$ docker service rm $SERVICE_ID
$ docker service ls
```

Stacks

```shell
$ docker stack deploy --compose-file myComposeFile.yml $NAME
$ docker stack ls
$ docker stack ps
$ docker stack rm
```

---
## Hands On

#### Exercises [here](https://github.com/mogensen/docker-handson-training/tree/master/3-Docker-swarm/Exercises.md)
