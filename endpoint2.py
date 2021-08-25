from botocore.vendored import requests
import json
import http.client
import random

def lambda_handler(event, context):
    # TODO implement
    response = requests.get("https://api.covid19api.com/live/country/mexico")
    data = response.json()
    random_number = int(random.uniform(1, 33))
    
    random_info = "Personas con covid en ",data[random_number]['Province'],": ", data[random_number]['Confirmed']
    
    
    return {
        'statusCode': 200,
        'body': json.dumps({"Estado": data[random_number]['Province'],"Casos Positivos Covid": data[random_number]['Confirmed']})
    }
