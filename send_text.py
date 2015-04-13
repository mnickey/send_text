""" Send text message version 2"""
import time # Needed to add the sleep timer

# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

#Set the auth token and sid for authentication by twillio client
auth_token = "PRIVATE"
account_sid = "PRIVATE"

# Create the client and authorize usage
client = TwilioRestClient(account_sid, auth_token)

TIME = 2700 # Time in seconds for sleep timer, 3600 seconds in an hour

if __name__ == "__main__":
     n = 130 # character count 
     TBC = " ... To Be Continued" #simple string to append at end of messages
     for chunk in (word[i:i+n] for i in range(0, len(word), n)): # Chunk the words string (paragraph) into easily manageable parts
          # create a message, send as body after attaching the chunk and TBC sending to 'TO' with from as you Twillio phone number
          sms = client.sms.messages.create(
               body=chunk + TBC, 
               to="**Private**",
               from_="+19258923347") 
          #Print the message sent to verify message delivery
          print chunk + TBC
          #Print the time the message was sent to verify message delivery
          print time.ctime()
          #Sleep for a specified time so you don't annoy the user. TIME specified in seconds
          time.sleep(TIME)
