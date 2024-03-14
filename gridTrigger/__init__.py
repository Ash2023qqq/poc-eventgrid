import logging
import json
from azure.functions import EventGridEvent
from typing import List
import azure.durable_functions as df


async def main(events: EventGridEvent, starter: str):
    client = df.DurableOrchestrationClient(starter)
    for event in events:
        #event = events
        #logging.info('Python Eventgrid trigger processed an event: %s', event.get_json())
        logging.info('Python Eventgrid trigger processed an event: %s', event.get_body().decode('utf-8'))
        #event_data = event.get_json()
        event_data = json.loads(event.get_body().decode('utf-8'))
        instance_id = await client.start_new('workflowOrchestrator', None, event_data)
        logging.info(f"Started orchestration with ID = '{instance_id}'.")
        print(f"Started orchestration with ID = '{instance_id}'.")       
