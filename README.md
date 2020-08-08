# Temperature-sensor

The optimum temperature range is a major factor in the industrial production of various drugs and other products.
Optimum temperature is required at various places at our homes also, like refrigerators.

#### So here is a project which will notify you via:
* SMS
* Email 
* Telegram

## Hardware Required
* Bolt IOT module
* LM35 Temperature Sensor
* USB to micro USB cable and an adaptor (To power up the module)
* 3 male-female jumper wires

## Software
* Python
* Telegram
* Gmail
* Twillo Cloud
* Bolt Cloud

### Set up to send temperature alert
Run following commands in python terminal:

> sudo apt-get -y update
> sudo apt install python3-pip
> sudo pip3 install boltiot

#### For sending alert via Email
In [Credential file](https://github.com/aawizard/Temperature-sensor/blob/master/Email/credentials.py)  fill the required details.

In terminal run the command
> python3 tempEmail.py

#### For sending alert via Telegram
...
#### For sending alert via SMS
...
