# driplet
(currently) microblog website

## Start the service via flask

`source venv/bin/activate`

`pip3 install -r requirements.txt`

`export FLASK_APP=microblog.py`

`python3 -m flask run`

## Start the service via docker

`docker build -t microblog:latest .`

`docker run --name microblog -p 8000:5000 --rm microblog:latest`

Then navigate to http://localhost:8000 to view the app.
