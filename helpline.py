import json
import urllib
import boto3

import random
import string

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.quote_plus(event['Records'][0]['s3']['object']['key'].encode('utf8'))
    try:
        response = s3.get_object(Bucket=bucket, Key=key)
        
        file_obj = event["Records"][0]
        filename = str(file_obj['s3']['object']['key'])
        
        fileObj = s3.get_object(Bucket='helpline-cmpe295', Key=filename)
        file_content = fileObj["Body"].read().decode("utf-8")
        
        file_json = json.loads(file_content)
        
        dynamo_db = boto3.resource('dynamodb')
        dynamoTable = dynamo_db.Table('temp')
        
        dynamoTable.put_item(Item = {
            'id': ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16)),
            'message': file_json['content'],
            'source': file_json['source'],
            'location': file_json['location'],
            'isrescued': file_json['isrescued'],
            'date': file_json['timestamp'],
            'category': file_json['area'], 
        })
        
        return "Lambda Working"
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
