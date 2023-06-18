import boto3

# Create an S3 client
session = boto3.Session(profile_name='account-name')
s3 = session.client('s3')

def create_bucket(bucket_name):
    # Create an S3 bucket with private access control
    response = s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-west-2'  # region
        },
        ACL='private'
    )
    print(f"Bucket created: {bucket_name}")

def upload_file(bucket_name, file_path, object_key):
    # Upload a file to the S3 bucket
    s3.upload_file(file_path, bucket_name, object_key)
    print(f"File uploaded: s3://{bucket_name}/{object_key}")

# Main
bucket_name = 'name'
file_path = '/path/'
object_key = 'file'

create_bucket(bucket_name)
upload_file(bucket_name, file_path, object_key)
