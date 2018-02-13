import boto3
from datetime import datetime

def handler(event, context):

    params = event['queryStringParameters']
    dynamodb = boto3.client('dynamodb')
    dynamodb.put_item(TableName="track", Item={'client_id': {'S':params['client_id']},
                                               'destination': {'S':params['destination']},
                                               'origin': {'S':params['origin']},
                                               'currency': {'S':params['currency']},
                                               'price': {'S':params['price']},
                                               'date': {'S':params['date']},
                                               'source_ip': {'S':event['requestContext']['identity']['sourceIp']},
                                               'timestamp': {'S':str(datetime.now())}})
    return {
        "statusCode": 200,
        "headers": {
            'Content-Type': 'image/gif'
        },
        "body": "R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7",
        "isBase64Encoded": True
    }
