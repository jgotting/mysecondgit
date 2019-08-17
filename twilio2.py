# -*- coding: utf-8 -*-
__author__ = 'Johan'

from twilio.rest import TwilioRestClient



client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
message = raw_input("Please enter your message: ")
message = client.messages.create(to="+46761354501", from_="+46108844886", body=message)
print(message.sid)
print("Ditt meddelande har skickats på nätet!")
print("Kolla din telefon är du snäll!")
