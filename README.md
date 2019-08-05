# SMSGateway

#### Prerequisites
Before you begin, make sure your development environment has `python3`installed.


###### Set Configuration
``` bash
# clone the repo
$ git clone https://github.com/ndungub/SMSGateway.git

# go SMSGateway folder
$ cd SMSGateway

# Set virtual enviroment
$ python3 -m venv smsenv

# install  dependencies
$ cd smsAPI
$ pip install -r dependencies.txt

# Set envriomental variables
$ sudo nano .env
```

#### Envirometal variables from `https://dashboard.nexmo.com/`
``` bash
FLASK_DEBUG=true
FLASK_SECRET_KEY=RANDOM-STRING_CHANGE-123-Ea359
NEXMO_NUMBER=YOUR_NUMBER
NEXMO_API_KEY=YOUR_KEY
NEXMO_API_SECRET=YOUR_SECRET_KEY
```

###### Set Configuration
``` bash
# Run the application
$ cd smsAPI
$ FLASK_APP=queue_sms.py flask run 

```
Fire the browser and use the url below:
http://127.0.0.1:5000/ or http://localhost:5000/




## Creators

**Boniface Ndungu**

* <https://twitter.com/ndungub_>
* <https://github.com/ndungub>

