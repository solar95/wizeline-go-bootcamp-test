from botocore.vendored import requests
import json
import http.client
import random



def lambda_handler(event, context):
    # TODO implement
    greeting = "Hello Wize Team!"
    
    
    return {
        'statusCode': 200,
        'body': json.dumps({"Greeting": gr})
    }
