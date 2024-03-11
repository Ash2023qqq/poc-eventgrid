# import os
# import json

# postreqdata = json.loads(open(os.environ['req']).read())
# print("Received events: {}".format(postreqdata))

# response = open(os.environ['res'], 'w')
# for event in postreqdata:
#     event_data = event['data']
#     print("Got a custom event {}".format(event_data))

# response.close()

import json
import logging

import azure.functions as func

def main(event: func.EventGridEvent):

    result = json.dumps({
        'id': event.id,
        'data': event.get_json(),
        'topic': event.topic,
        'subject': event.subject,
        'event_type': event.event_type,
    })

    logging.info('Python EventGrid trigger processed an event: %s', result)
