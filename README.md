# Endpoint for search

## Python & Django setup

* Install `python3` via brew
* Clone the repo
* cd into repo
* Install `virtualenv` using `pip3`

```sh
sudo pip3 install virtualenv
```

* Create a virtualenv for the project

```sh
virtualenv -p python3 venv
```

If you're having trouble completing this step, try upgrading virtualenv first `pip3 install --upgrade virtualenv`

* Activate the virtualenv

```sh
source venv/bin/activate
```

* Install dependencies in the new virtualenv

```
pip3 install -r requirements.txt
```

```
python3 manage.py runserver
```

* Testing

```
python3 manage.py test
```

* Server should be running at http://localhost:8000

Query params that are accepted are: searchTerm, lat and lng

Try visiting: http://localhost:8000/search?searchTerm=camera&lat=51.948&lng=0.172943

