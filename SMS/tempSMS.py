import credentials
import json
import time
from boltiot import Sms, Bolt
minimum_limit = 300 
maximum_limit = 600
mybolt = Bolt(credentials.API_KEY, credentials.DEVICE_ID)
sms = Sms(credentials.SID, credentials.AUTH_TOKEN, credentials.TO_NUMBER, credentials.FROM_NUMBER)
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
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is " +str(Temperature))
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)



