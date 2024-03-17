import json
import logging
import datetime
import azure.functions as func

def main(event: str, outputEvent: func.Out[func.EventGridOutputEvent]):
    #logging.log("eventGridEvent: ", event)
    logging.info('Python EventGrid trigger received an incoming event: %s', event)
    # result = json.dumps({
    #     'id': "event.id",
    #     'data': event,data={"tag1": "value1", "tag2": "value2"},
    #     'topic': "event.topic",
    #     'subject': "event.subject",
    #     'eventtype': "event.eventtype",
    # })
    result = json.loads(event)
    outputEvent.set(
        func.EventGridOutputEvent(
            id="result.id",
            data=result,
            subject="result.subject",
            event_type="result.eventtype",
            event_time=datetime.datetime.utcnow(),
            data_version="1.0"))
    logging.info('Python EventGrid trigger processed an event: %s', result)
    return 0
