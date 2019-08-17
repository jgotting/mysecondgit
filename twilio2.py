# -*- coding: utf-8 -*-
__author__ = 'Johan'

from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "ACeb16b14b52886960c4b521d48547c17c"
AUTH_TOKEN = "09f114f92bfa404cefc50d319a0d8d9a"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
message = raw_input("Please enter your message: ")
message = client.messages.create(to="+46761354501", from_="+46108844886", body=message)
print(message.sid)
print("Ditt meddelande har skickats på nätet!")
print("Kolla din telefon är du snäll!")
