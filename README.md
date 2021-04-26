# API for the Wazuh Technical test
In this project, I have built an API that presents data from the file `assets/alerts.json` through a series of endpoints.

## Installation
These instructions are meant to be followed in a linux CLI

### Clone this repository and access the directory
```
git clone https://github.com/mpRegalado/wazuhTechnicalAPI
cd wazuhTechnicalAPI
```
### Optional: Create a virtual python enviroment and enable it
```
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```
### Install dependencies
```
pip3 install -r requirements.txt
```

## Usage
All done!
You can run the api by running
```
FLASK_APP=app flask run
```
The endpoints should be available at `http://127.0.0.1:5000`

Or you may run the unit tests with
```
pytest -v
```