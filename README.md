# Creating a Docker Project

First create a Dockerfile to tell Docker what to do.

Inside project directory use the command

```
$ touch Dockerfile
```

Using Alpine Linux allows us to start with a smaller instance.

Inside the Docker file add the commands

```
FROM alpine
CMD ['echo hello world']
```