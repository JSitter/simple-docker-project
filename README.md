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
CMD ["echo", "Hello World!"]
```

To build the project run

```
docker build -t my-container:latest .
```

You should see some output to the screen like this.

```
Successfully built ec6498e61d1a
```

This is the id for the container.

Use this id to launch the container.

```
docker run my-container-name
```

You should see the text.

```
Hello World!
```

## Create a Python Project

Change the Dockerfile for Python

```
FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
```
Run the command 

```
docker build -t my-python-project
```

and 

```
docker run my-python-project
```