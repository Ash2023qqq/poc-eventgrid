import os
import json

postreqdata = json.loads(open(os.environ['req']).read())
print("Received events: {}".format(postreqdata))

response = open(os.environ['res'], 'w')
for event in postreqdata:
    event_data = event['data']
    print("Got a custom event {}".format(event_data))

response.close()
