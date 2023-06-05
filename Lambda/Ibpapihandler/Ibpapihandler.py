import json
import boto3
import os

def handler(event, context):
    ddb = boto3.resource('dynamodb')
    ddbitem = {}
    print("Received event: " + json.dumps(event, indent=2))
    RequestID = event['queryStringParameters']['RequestID']
    ddbConfigTable = ddb.Table(os.environ.get('DDB_CONFIG_TABLE'))
    ddbitem['RequestID'] = RequestID
    ddbitem['Status']= "Initial"
    ddbConfigTable.put_item(Item=ddbitem)
    return {         # <---- RETURN THIS RIGHT AWAY
            'statusCode': 200 ,
            "headers": {
        'Content-Type': 'text/html',
    },
            'body':"Hello IBP, processing triggered"        
            
    }
    #return "Hello world"
