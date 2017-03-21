from twilio.rest import TwilioRestClient

account_sid = "ACb847967d02eeae68c625fe4a82406288" # Your Account SID from www.twilio.com/console
auth_token  = "80a909e83a826236bfc759180888e28e"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
	message = client.messages.create(to="+919587460894",    # Replace with your phone number
    	from_="+19373299177",body="Hi, There is a job opportunity for you according to your qualification. Please visit https://www.linkedin.com/jobs/view/271169980/ ")
	print(message.sid)

except TwilioRestException as e:
    print(e)