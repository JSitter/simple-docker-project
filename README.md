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
$ docker build -t my-container:latest .
```

You should see some output to the screen like this.

```
Successfully built ec6498e61d1a
```

This is the id for the container.

Use this id to launch the container.

```
$ docker run my-container-name
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

Also in the project root should be a file named `requirements.txt` that contains these dependencies:

```
flask
flask_restplus
```

Replace the contents of Dockerfile with

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
$ docker build -t my-python-project
```

and 

```
$ docker run my-python-project
```

## Deploying to Heroku

Deploying to Heroku is a little different than the typical way.

```
$ heroku login
```

Push the container to Heroku using the command:

```
$ heroku container:push web -a my-heroku-app-name
```

After it's pushed and built on Heroku, it must be released. 

```
$ heroku container:release web -a my-heroku-app-name
```

## Scale your App
Heroku will scale your app to 0 by default.

Scale your app depending on your tier.

```
$ heroku ps:scale web=1
```

View the working application by typing

```
$ heroku open
```

View this code in [a production environment](http://simple-docker-app.herokuapp.com).