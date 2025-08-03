import boto3
import os

def process_file():
    s3 = boto3.client('s3')
    bucket = os.environ['BUCKET']
    input_key = os.environ['INPUT_KEY']
    output_key = f"output/{input_key.split('/')[-1]}"

    file_obj = s3.get_object(Bucket=bucket, Key=input_key)
    content = file_obj['Body'].read().decode('utf-8')
    content = content.upper()

    s3.put_object(Bucket=f"{bucket}-output", Key=output_key, Body=content.encode('utf-8'))

if __name__ == "__main__":
    process_file()
