# Creating a Docker Project

First create a Dockerfile to tell Docker what to do.

Inside the project directory use the command:

```
$ touch Dockerfile
```

Alpine Linux allows us to start with a very light weight linux distro.

The Dockerfile contains all the commands we'll need to start up our application. Here is a demonstration of Hello World using an Alpine linux container.

Inside `Dockerfile` add these commands:

```
FROM alpine
CMD ["echo", "Hello World!"]
```

Build the project by running:

```
$ docker build -t my-container:latest .
```

You should see some output to the screen like this:

```
Successfully built 3373beab55ed
Successfully tagged my-container:latest
```

Then simply launch the container.

```
$ docker run my-container
```

You should see the text.

```
Hello World!
```

## Create a Python Project

Create these two required files.

`app.py` should be in the project root directory and should contain this:

```
from flask_restplus import Api, Resource, fields
from flask import Flask, request, jsonify

app = Flask(__name__)
api = Api(app, version='1.0', title='Simple Flask App', description='This is a flask app for flasking things and apping')
ns = api.namespace('Flask Space', description='Methodical methods')

single_parser = api.parser()

@ns.route('/')
class Index(Resource):
  ''' Main page.'''
  @api.doc(parser=single_parser, description='Get main page')
  def get(self):
    return {"Who did it?": "Don't Ask"}

if __name__ == '__main__':
  PORT = int(os.environ.get('PORT', 8000))
  app.run(host='0.0.0.0', port=PORT)
```

Also in the project root there should be a file named `requirements.txt`. This file contains a list of these dependencies:

```
flask
flask_restplus
```

Then replace the contents of Dockerfile with:

```
FROM python:3.6
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
```

This container uses an Ubuntu system with python 3.6 already installed.

Build and tag the container:

```
$ docker build -t my-python-project
```

Run the container:

```
$ docker run my-python-project
```

## Deploying to Heroku

Deploying a Docker project on Heroku is a little different than just pushing a generic flask app. Make sure you're logged into Heroku in the cli tool.

```
$ heroku login
```

After the login process for Heroku, you'll need to login to your container registry.

```
$ heroku container:login
```

Push the container to Heroku using the command:

```
$ heroku container:push web -a my-heroku-app-name
```

After it's pushed and built on Heroku, it must be released.

```
$ heroku container:release web -a my-heroku-app-name
```

### Scale your App
Heroku will scale your app to 0 by default and this won't work.

Scale your app depending on your tier. This scales it for the free tier.

```
$ heroku ps:scale web=1
```

View the working application by typing

```
$ heroku open
```

If the application doesn't appear, make sure that the proper port is being exposed.

Heroku uses an environment variable `PORT` which holds the value for the port to expose.

Make sure your app is listening on this port in order to accept incoming connections.

View this code in [on Heroku](http://simple-docker-app.herokuapp.com).

## Use Docker to Run a Database

This example will use MySQL, but any other database can be used instead.

```
$ docker run --detach --name=my-db-name --env="MYSQL_ROOT_PASSWORD=environmentpasswor4d" mysql
```

You should get a container with a mysql instance running.

Check out the details of the instance by running

```
$ docker inspect my-db-name
```

There is a great [medium article](https://medium.com/coderscorner/connecting-to-mysql-through-docker-997aa2c090cc) about the use of mysql and phpmyadmin using docker containers. One caveat is that the newest version of MySQL may require an authorization that phpmyadmin does not understand. Therefore, it's a good idea to make sure that you specify compatible versions of the two pieces of software to avoid issues.

## Add Heroku Compatible MySQL Support

Add dependencies to the `requirements.txt` file:

```
SQLAlchemy
flask-bcrypt
```
