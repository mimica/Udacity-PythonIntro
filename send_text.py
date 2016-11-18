from twilio.rest import TwilioRestClient

account_sid = "ACaf8cc9cb79e09d2e7eb80067754903ea"
auth_token = "a0a722f36ed2600bc632f4b742b5d4c0"
client = TwilioRestClient(account_sid, auth_token)

#message = client.sms.messages.create(
#	body="Testing, 123",
#	to="+5521981698875",
#	from_="+14243216402")

message = client.messages.create(
        to = "+5521981698875",
        from_ = "+14243216402",
        body = "Testing, 123")

print message.sid