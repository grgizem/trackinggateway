# Tracking Gateway

## Installation
```
# git clone git@github.com:grgizem/trackinggateway
# export S3Bucket=<bucket-name>
# zip lambda.zip lambda.py
# aws s3 cp lambda.zip s3://$S3Bucket/
```

Create your db, lambda function and API gateway with,
```
# aws cloudformation create-stack --stack-name apigateway --template-body file://cf_template.json --capabilities CAPABILITY_IAM --parameters ParameterKey=S3Bucket,ParameterValue=$S3Bucket
```

## Deployment
After creating API Gateway add 'image/gif' to "Binary media types" in the API Gateway console and deploy API.

Copy Invoke Url and paste on test.html file and try on your browser.

You can also test is manually by calling invoke url as follows,
https://<INVOKE_URL>/track.gif?client_id=123&origin=IST&destination=JFK&price=500&currency=TRY&date=20/01/2019

You can check 1x1 pixel image with,
```
curl -H "Accept:image/gif" "https://<INVKE_URL>/track.gif?client_id=123&origin=IST&destination=JFK&price=500&currency=TRY&date=20/01/2019" --output track.gif
```