from twilio import rest
account_sid=""
auth_token=""
client=rest.TwilioRestClient(account_sid,auth_token)

message=client.sms.messages.create(body="Hi thi is khushali",to="+11234567899",from_="+12222222222")
print message.sid