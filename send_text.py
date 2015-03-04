""" Send text message """
import time # Needed to add the sleep timer

auth_token = "PROVIDED BY TWILLIO UPON SIGNING UP"
account_sid = "PROVIDED BY TWILLIO UPON SIGNING UP"

# install and sign up for twillio; docs can be found here: twilio.com/docs/python/install
from twilio.rest import TwilioRestClient
 
# Pass in the account_sid & auth tokens
client = TwilioRestClient(account_sid, auth_token)

# Use only 160 characters per line.
body1 = "Rachelle! I love you <3. In the short time that we've been together I am amazed each day that we spend together. You are my everything. To be continued..."
body2 = "I've never felt so compelte and wonderful. You have changed my heart and opened my eyes to new & wonderful opportunities. To be continued..."
body3 = "I want nothing more than to make you happy so I can see that beautiful smile. You truly are my Wonder Woman. Kisses -- MEN" 
# Add the messages to a list to itterate over
body_list = [body1, body2, body3]

TIME = 9000 # Time in seconds for sleep timer -- 9000 seconds is 2.5 hours

count = 0
while count < 3:
	sms = client.sms.messages.create(
		body=body_list[count],
		to="+1 THIS IS YOUR RECIPIENTS PHONE NUMBER PREFIXED WITH A 1", 
		from_="+1 THIS IS YOUR TWILIO PHONE NUMBER PREFIXED WITH A 1") 
	print body_list[count] # printing just to check and make sure they are sent
	count += 1 # increase the count to avoid infinite loops
	print sms.sid # printing the sms ID for message verification
	time.sleep(TIME) # use times sleep function to sleep before next execution
