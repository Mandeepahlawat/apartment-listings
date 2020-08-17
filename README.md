# README

## Instructions:

#### Steps to setup app:

* Navigate to project folder in terminal
* Create new virtual env
```
python3 -m venv env
```
* Activate new virtual env
```
source env/bin/activate
```
* Install requirements
```
pip install -r requirements.txt
```


#### Features:

* Mapped CSV data into Django Models
* Created a command to import csv data from terminal.
* To import data into Django Models use following command
```
./manage.py import_data
```
* Data import command accepts an optional filename option. If specified it uses the filename specified in the option, otherwise it users default csv file names "challenge_data.csv".
* Created a command to delete all data.
```
./manage.py delete_data
```
* Created API endpoints with CRUD operations on all the Models.
* To view all API endpoints and to play around with the data you need to run the server and navigate to "http://127.0.0.1:8000/api/"
* To run server use following command:
```
./manage.py runserver
```

#### Scalability:
* CSV data is broken down into different individual models, which provide future scope to include new external source, other than "zellow".
* Scope to add new Area units in future.
* Scope to add new Home types in future.
* Location data can be used separately. We can add new State, City or ZipCodes.


#### Future work:

* Add test cases API endpoints.
* Better exception handling for importing data.
* Develop frontend for APIs in React