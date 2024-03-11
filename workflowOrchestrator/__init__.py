import logging
import json

from azure.durable_functions import DurableOrchestrationContext, Orchestrator


def orchestrator_function(context: DurableOrchestrationContext):
    event_data = context.get_input()
    logging.info(f"workflow_orchestrator invoked, received event_data: {event_data}")
    print(f"workflow_orchestrator invoked, received event_data: {event_data}")
    model_requested = event_data["model"]
    if model_requested == "consumer":
        result = yield context.call_activity("consumer", model_requested)
    #elif model_requested == "aiaas_sda_vitals":
    #    result = yield context.call_activity("aiaas_sda_vitals", event_data)
    else :
        result = "Model not found"
    return result

main = Orchestrator.create(orchestrator_function)
