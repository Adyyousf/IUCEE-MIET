# Project Title
 IUCEE-MIET 
## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Authors](#authors)

## About <a name = "about"></a>

A complete website built in django for IUCEE-MIET

## Getting Started <a name = "getting_started"></a>

Start by installing the dependencies included in the requirements.txt file.
See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

All prerequisites are included inside requirements.txt

### Installing

clone this file inside a project folder and install virtualenv and create virtual environment
```
$ cd IUCEEweb
$ pip install virtualenv
$ virtualenv <projectname> 

```

activate the virtualenv and install dependencies

```
$ source <projectname>/Scripts/activate
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000

## ✍️ Authors <a name = "authors"></a>
- [@Adyyousf](https://github.com/Adyyousf) - Idea & Initial work
