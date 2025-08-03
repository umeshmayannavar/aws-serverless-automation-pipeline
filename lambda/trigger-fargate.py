import boto3
import os
import json

ecs = boto3.client('ecs')
region = os.environ['AWS_REGION']
cluster = os.environ['CLUSTER_NAME']
subnet = os.environ['SUBNET_ID']
security_group = os.environ['SECURITY_GROUP_ID']
task_definition = os.environ['TASK_DEF']

def lambda_handler(event, context):
    for record in event['Records']:
        key = record['s3']['object']['key']
        response = ecs.run_task(
            cluster=cluster,
            launchType="FARGATE",
            taskDefinition=task_definition,
            count=1,
            platformVersion='LATEST',
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': [subnet],
                    'securityGroups': [security_group],
                    'assignPublicIp': 'ENABLED'
                }
            },
            overrides={
                'containerOverrides': [
                    {
                        'name': 'file-processor',
                        'environment': [
                            {'name': 'INPUT_KEY', 'value': key},
                            {'name': 'BUCKET', 'value': os.environ['BUCKET']}
                        ]
                    }
                ]
            }
        )
        print(f"Triggered ECS task for: {key}")
    return {"statusCode": 200}
