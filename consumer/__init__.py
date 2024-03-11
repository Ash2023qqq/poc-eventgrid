import json
import logging

import azure.functions as func

def main(event: str):

    result = json.dumps({
        'id': "event.id",
        'data': event,
        'topic': "event.topic",
        'subject': "event.subject",
        'event_type': "event.event_type",
    })

    logging.info('Python EventGrid trigger processed an event: %s', result)
    return result
