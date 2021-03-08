# Web Framework with Flask
Flask is a flexible micro web framework written in Python. It aims to keep the core of the application simple, and unlike some other frameworks, makes no decisions for you.  Flask supports extensions such as database integration, form validation, user authentication, and many more.  

## Setting up the directory
By convention, templates and static files are stored in subdirectories within the application's source tree, with the names `templates` and `static`. The more complex the project is, the more directories are used for organization. This workshop will focus on quick single module projects. A simple project tree could look like this:

```
app.py
config.py
requirements.txt
static/
templates/
```
Application logic would go in the app.py file.


## A simple app
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello, World!"

if __name__=='__main__'
	app.run(debug = True)
```

We import the Flask module and instantiate the application.  Next, we use the `route()` decorator to tell Flask what URL should trigger our function. The function is given a name which is also used to generate URLs for that particular function and returns the message we want to display.  Lastly, running the app in debug mode allows us to easily see the changes we make without restarting the server.


## Routes
The `route()` decorator is used to bind a function to a URL.
```
@app.route('/')
def hello():
	return "Hello, World!"

@app.route('/about')
def about():
	return 'the about page'
```

## Templates
Generating HTML from within Python can be very cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that, Flask configures the Jinja2 template engine for you automatically. To render a template you can use the `render_template()` method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.
```
from flask import render_template

@app.route('/hello/')
def hello():
    return render_template('hello.html')
```
The most powerful part of Jinja is template inheritance. This allows you to build a base template that contains all the common elements of your site and defines blocks that child templates can override. Jinja uses {% %} for notation. The layout template could look like this:
```
<!DOCTYPE html>

<html>
    <head>
        <title></title>
    </head>
        {% with messages = get_flashed_messages() %}
            {% if messages %}
                {% for message in messages %}
                    {{ message }}
                {% endfor %}
            {% endif %}
        {% endwith %}
    <body>
        {% block body %}{% endblock %}
    </body>
</html>
```
The {% block %} tags define blocks that child templates can fill in. Subsequent templates would be as simple as this:
```
{% extends "layout.html" %}

{% block body %}
    Welcome to my homepage!
{% endblock %}
```
The {% extends %} tag locates the parent template for rendering.


## HTTP Methods
Web applications use different HTTP methods when accessing URLs. You can use the methods argument of the `route()` decorator to handle different HTTP methods. By default, a route only answers to GET requests. Use a POST request with sensitive information.
```
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

## Bootstrap
This workshop focused more on the back-end framework but many flask applications use Bootstrap for front-end styling.  Many customizable layouts can be implemented in your templates for a better look.

## Examples
1. Sign up for GUS 8066 with the flask-wtf extension
2. Areal Weighting Interpolation

[Flask documentation:](https://flask.palletsprojects.com/en/1.1.x/)
[Jinja2 documentation:](https://jinja.palletsprojects.com/en/2.11.x/templates/)
[Bootstrap:](https://getbootstrap.com/)
