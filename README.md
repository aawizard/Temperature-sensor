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

## Software Required
* Python
* Telegram
* Gmail
* Twillo Cloud
* Bolt Cloud

## Hardware Connections
![Hardware Connections](https://cdn.fs.teachablecdn.com/resize=width:400/Ig2OOt38Tn28UQro2CT0)

## Set up to send temperature alert
Run following commands in python terminal:

> sudo apt-get -y update
> sudo apt install python3-pip
> sudo pip3 install boltiot

### For sending alert via Email
In [Credential file](https://github.com/aawizard/Temperature-sensor/blob/master/Email/credentials.py)  fill the required details.

In terminal run the command
> python3 tempEmail.py

### For sending alert via Telegram
* Create a telegram bot
* Create a new channel
* Add bot to the channel as administrator
* Fill all the details in [Configuration file](https://github.com/aawizard/Temperature-sensor/blob/master/Telegram/conf.py)
* In terminal run the command
> python3 tempTelegram.py

### For sending alert via SMS
* Create a account on Twillo 
* Create a new project 
* From the twillo project copy API key, SID and phone number and fill in [Credential file](https://github.com/aawizard/Temperature-sensor/blob/master/SMS/credentials.py)
* In terminal run the command 
> python3 tempSMS.py
