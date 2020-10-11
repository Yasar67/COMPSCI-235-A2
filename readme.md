# COVID-19 Web Application

## Description

A Web application that demonstrates use of Python's Flask framework. The application makes use of libraries such as the Jinja templating library and HTML forms. Architectural design patterns and principles including Repository and Dependency Inversion have been used to design the application. The application uses Flask Blueprints to maintain a separation of concerns between application functions.

## Installation

**Installation via requirements.txt**

```shell
$ python -m venv venv
$ ./venv/bin/activate
$ pip install -r requirements.txt
```

*MacOS specific setting*
When using PyCharm, set the virtual environment using 'PyCharm'->'Preferences' and select 'Project: *Your Root Folder Name* from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution

**Running the application**

From the *A2* directory, and within the activated virtual environment:

````shell
$ flask run
```` 


## Configuration

The *A2/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.
