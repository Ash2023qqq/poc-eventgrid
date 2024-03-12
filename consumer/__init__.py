import json
import logging
import datetime
import azure.functions as func

def main(event: str, outputEvent: func.Out[func.EventGridOutputEvent]):
    logging.log("eventGridEvent: ", event)
    # result = json.dumps({
    #     'id': "event.id",
    #     'data': event,
    #     'topic': "event.topic",
    #     'subject': "event.subject",
    #     'eventtype': "event.eventtype",
    # })
    outputEvent.set(
        func.EventGridOutputEvent(
            id="test-id",
            data={"tag1": "value1", "tag2": "value2"},
            subject="test-subject",
            event_type="test-event-1",
            event_time=datetime.datetime.utcnow(),
            data_version="1.0"))
    logging.info('Python EventGrid trigger processed an event: %s', event)
    return 0
