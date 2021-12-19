# AWS-Lambda-Fuction-S3-DynamoDB
An AWS Lambda function which gets triggered whenever a new file gets uploaded to an S3 bucket and then uploads the data to a DynamoDB table

Steps to run
Create a Lambda function in AWS Management Console.
Assign a role to the Lambda function and make sure it has read access for S3 and write access for DynamoDB
You can reconfigure the code to append it to your project flow. See the AWS Lambda documentation for more details.
You can remove the print statements which were for debugging purposes. If you want to see the log messages then you would also have to grant access for the CloudWatch to the lambda function
Please feel free to open a PR for bug fixes or exntesions.
