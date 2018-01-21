import RPi.GPIO as GPIO
import time
import json
import requests

try:

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(4,GPIO.IN)
	
	# insert your slack webhook url here
        webhook_url="XXXXXXX"
        slack_msg= { 'text': ":bangbang: Tripwire Tripped"}
	
	prevState=0
	currState=0
	tripped=0

	while True:
                # get current state
		currState=GPIO.input(4)

                # Determine if tripped
		if prevState == 0 and currState == 1:
			tripped=1
			prevState=1

                # reset upon state change
		if prevState == 1 and currState == 0:
			prevState=0
			
                # if tripped, Slack it!
		if tripped == 1:
			print "Tripped"
			r = requests.post(webhook_url, data=json.dumps(slack_msg))
			print(r.status_code, r.reason)
			tripped=0

                # slow it down
		#time.sleep(1)
	
except KeyboardInterrupt:
	print "exiting"
finally:
	GPIO.cleanup()


