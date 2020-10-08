# Carisk Backend

<p align="center">
  <img src="https://i.imgur.com/2RFEstw.png">
</p>

Backend deploy can found [here](https://does-not-exist-yet.com/)

Website can be found [here](https://does-not-exist-yet.com/)

## Project links

[Frontend](https://github.com/Carisk/Carisk-Frontend) 

## Info

This backend works with django 3.0.6 and python 3.7

## How to setup?

1. First create a virtual environment for python3 with

```
python3 -m venv ve
```

Name it `ve` or if you decide to name it something else, remember to **never commit the
virtual enviroment folder**.

2. Enter the virtual environment

```
source ve/bin/activate
```

3. Install the dependencies if it's your first time installing it

```
pip install -r requirements.txt
```

## How to run?

1. Enter the virtual environment

```
source ve/bin/activate
```

2. Now run with

```
python manage.py runserver
```

3. Stopping

Stop the server with `CTRL+C` and exit the virtual env with 

```
deactivate
```
