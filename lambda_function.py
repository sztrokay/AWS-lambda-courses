import json
import requests

def lambda_handler(event, context):
    url = "https://script.google.com/macros/s/AKfycbzG-rJapGn5WwiCSW19exulOGSZipNRwGG1H75wP-RxRnJjP7DoQig5lSlqhdlzjmFr/exec"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    return {
        'statusCode': 200,
        'headers':{
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, GET'
        },
        'body': parsed
    }