# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------
"""
FILE: publish_event_grid_events_to_custom_topic_sample.py
DESCRIPTION:
    These samples demonstrate creating a list of Eventgrid Events and sending them as a list
    to custom topic.
USAGE:
    python publish_event_grid_events_to_custom_topic_sample.py
    Set the environment variables with your own values before running the sample:
    1) EVENTGRID_TOPIC_KEY - The access key of your eventgrid account.
    2) EVENTGRID_TOPIC_ENDPOINT - The topic hostname. Typically it exists in the format
    "https://<YOUR-TOPIC-NAME>.<REGION-NAME>.eventgrid.azure.net/api/events".
"""
import os
from random import randint, sample
import time

from azure.core.credentials import AzureKeyCredential
from azure.eventgrid import EventGridPublisherClient, EventGridEvent

key = os.environ["EVENTGRID_TOPIC_KEY"]
endpoint = os.environ["EVENTGRID_TOPIC_ENDPOINT"]

# authenticate client
credential = AzureKeyCredential(key)
client = EventGridPublisherClient(endpoint, credential)
services = ["EventGrid"]    # possible values for data field

def publish_event():
    # publish events

    event_list = []     # list of events to publish
    # create events and append to list
    event = EventGridEvent(
            subject="ModelResponse",
            data={"make": "Ferrari", "model": "Classy"},
            event_type="Model.Response",
            data_version="2.0"
            )
    event_list.append(event)

    # publish list of events
    client.send(event_list)
    print("Batch of size {} published".format(len(event_list)))
    time.sleep(randint(1, 5))

if __name__ == '__main__':
    publish_event()
