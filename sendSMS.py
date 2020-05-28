from twilio.rest import Client
from credentials import accountSid, authToken, myCell, myTwilio   #importing data from credentials.py

client = Client(accountSid,authToken)  

messageBody = "Hello I am XYZ"  #you can customize your message as per your need.

message = client.messages.create(to = myCell, from_= myTwilio,body = messageBody)  #create is an method to create message