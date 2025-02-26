# Web Framework with Flask

Flask is a micro web framework written in Python. It aims to keep the core simple, and unlike some other frameworks, makes no decisions for you.  Flask supports extensions such as database integration, form validation, and user authentication.

## Setting up the directory

By convention, templates and static files are stored in subdirectories within the application's source tree, with the names `templates` and `static`. The more complex the project is, the more directories are used for organization. This workshop will focus on quick single module projects. The project tree could look like this:

```
app.py
config.py
requirements.txt
static/
templates/
```

Application logic would go in the app.py file.


## A simple app

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__"
    app.run(debug = True)
```

We import the Flask module and instantiate the application.  Next, we use the `route()` decorator to tell Flask what URL should trigger our function. The function is given a name which is also used to generate URLs for that particular function and returns the message we want to display.  Lastly, running the app in debug mode allows us to easily see the changes we make without restarting the server.

After examining the `flask_hello.py` script file, open the Anaconda Prompt and activate a conda environment with Flask installed (such as our course environment). Navigate to the `flask_hello` folder. Load the web application with:

```sh
flask --app flask_hello run

# # Alternatively:
# python flask_hello.py
```

Note the messages in the terminal:

```sh
 * Serving Flask app 'flask_hello'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

Then in your web browser, navigate to <http://127.0.0.1:5000>.

When you have confirmed that it working correctly, press <kbd>Ctrl</kbd> + <kbd>C</kbd> to quit.

A list of the additional demo apps appears at the bottom of this document.

## Routes

The `route()` decorator is used to bind a function to a URL.

```python
@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/about')
def about():
    return "the about page"
```

## Templates

Generating HTML from within Python can be very cumbersome because you have to do the HTML escaping on your own to keep the application secure. Because of that Flask configures the Jinja2 template engine for you automatically. To render a template you can use the `render_template()` method. All you have to do is provide the name of the template and the variables you want to pass to the template engine as keyword arguments.

Note that this example does not exist in the workshop folder. You could create a template `hello.html` containing the text "Hello, World!" to render, but we will explore static web pages in the `flask_map` app.

```python
from flask import render_template

@app.route("/hello")
def hello():
    return render_template("hello.html")
```

Usually, however, we don't just stick static web pages in the template folder. The most powerful part of Jinja is template inheritance. This allows you to build a base template that contains all the common elements of your site and defines blocks that child templates can override. Jinja uses {% %} as notation.

```html
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

The {% block %} tags define blocks that child templates can fill in. Notice how common Python looping and conditionals can be used.  Be sure to close with the appropriate notation.  For example {% for...%} {% endfor %} 

```
{% extends "layout.html" %}

{% block body %}
    Welcome to my homepage!
{% endblock %}
```

The {% extends %} tag locates the parent template for rendering.


## HTTP Methods

Web applications use different HTTP methods when accessing URLs. You can use the methods argument of the `route()` decorator to handle different HTTP methods. By default, a route only answers to GET requests. Use a POST request with sensitive information.

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

## Bootstrap

This workshop focused more on the back-end framework but many flask applications use Bootstrap for front-end styling.  Many customizable layouts can be implemented in your templates for a better look.  Here's an example of a template that uses a navigation bar from Bootstrap.

```html
<!DOCTYPE html>

<html>
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">
        <title></title>
    </head>
    <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
        </li>
      </ul>
      <form class="d-flex">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/js/bootstrap.bundle.min.js" integrity="sha384-b5kHyXgcpbZJO/tY9Ul7kGkf1S0CWuKcCD38l8YkeH8z8QjE0GmW1gYU5S9FOnJ0" crossorigin="anonymous"></script>
    {%block body%}{%endblock%}
    </body>
</html>
```

You would then extend this layout to any template using the notation mentioned above.

## Examples

1. Hello, world: `flask_hello`
2. Loading more complex, static web pages: `flask_map`
3. Simple form: `flask_buttons`
4. Simple API: `flask_api`
    * Acceptable years are 2020 and 2021

In each case, navigate to the indicated folder and call `python script.py` at the command line. Then load <http://127.0.0.1:5000/> in your web browser.


<!--
1. Sign up for GUS 8066 with the flask-wtf extension
2. Areal Weighting Interpolation

## Further exploration with Flask
1. User Authentication
2. Database Access/Management

-->

## Some Notes

Examples above and many examples online (including the Folium documentation, see below) put `app.run()` in the module as follows:

```python
if __name__ == "__main__":
    app.run(debug = True)
```

Then the module is called with

```sh
python module_name.py
```

Our textbook (*WGPD*) and the [Flask Quickstart](https://flask.palletsprojects.com/en/stable/quickstart/) do *not* put `app.run()` in the module, and instead start Flask explicitly with:

```sh
flask --app module_name run
```

If the module is named `app.py`, the name can be omitted.

The `FLASK_APP` name (the module) can also be set as an environment variable. The textbook shows setting this environment variable every time you run the app. Since we are running Flask in a conda environment, you can permanently set environment variables *for that specific conda environment*. To set the necessary variables for the textbook examples, you can run the following command in the conda environment where you are running flask:

```sh
conda env config vars set FLASK_ENV=development FLASK_APP=app.py
```

Then you can run Flask without having to specify the module:

```sh
flask run
```

The textbook *briefly* covers running Flask in a production environment using `gunicorn`. The Flask documentation goes into more detail with links to several options for deploying Flask to production web server, including options for cloud hosting: <https://flask.palletsprojects.com/en/stable/deploying/>.

Since this is a GIS course, you may be interested in using Flask for web map deployment. The Folium documentation has an intro to [Using folium with flask](https://python-visualization.github.io/folium/latest/advanced_guide/flask.html).


## Documentation

* [Flask documentation](https://flask.palletsprojects.com/en/stable/)
* [Jinja2 documentation](https://jinja.palletsprojects.com/en/2.11.x/templates/)
* [Bootstrap](https://getbootstrap.com/)
