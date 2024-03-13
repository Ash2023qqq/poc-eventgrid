import json
import logging
import datetime
import azure.functions as func

def main(event: func.EventGridEvent):
    result = json.dumps({
        'id': "event.id",
        'data': event.get_json(),
        'topic': "event.topic",
        'subject': "event.subject",
        'eventtype': "event.eventtype",
    })
    print(result)
    logging.info('Python EventGrid trigger : The acknowledgment from the ack topic is processed: %s', event)
    #return result
