import credentials
import json
import time
import smtplib, ssl
from boltiot import Sms, Bolt

port = 465
minimum_limit = 350 
maximum_limit = 500
mybolt = Bolt(credentials.API_KEY, credentials.DEVICE_ID)
sender_email=credentials.email_ID
reciever_email=""     #Add email to which you have to sand email
password=credentials.password
message = """\
Subject: Alert!!!

The temperature is """

# Create a secure SSL context

while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    #print (response)
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        Temperature=(100*sensor_value)/1024 
        #print(Temperature)
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Sending Email")
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, reciever_email, message+str(Temperature)+"C")

            
            
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)


