import json
import logging
import datetime
import azure.functions as func

def main(event: func.EventGridEvent):
    try:
        result = json.dumps({
            'id': "event.id",
            'data': "event.data",
            'topic': "event.topic",
            'subject': "event.subject",
            'eventtype': "event.event_type",
        })
        print(result)
        logging.info('Python EventGrid trigger : %s', result)
        logging.info('Python EventGrid trigger : The acknowledgment from the ack topic is processed: %s', event)
    #return result
    except Exception as e:
        logging.error(f'Unhandled error: {str(e)}')
