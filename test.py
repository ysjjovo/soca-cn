import boto3 
from botocore.client import ClientError
s3 = boto3.session.Session().resource("s3")
client = boto3.client('s3')

def check_bucket_permission(bucket):
    # Check if user has permission to the S3 bucket specified
    try:
        s3.meta.client.head_bucket(Bucket=bucket)
        client.get_bucket_ownership_controls(
            Bucket=bucket,
            ExpectedBucketOwner='260527533511'
        )
        return True
    except ClientError as e:
        error_code = int(e.response['Error']['Code'])
        if error_code == 404:
            try:
                s3.Bucket(bucket).create()
                print(f"Create new Bucket {bucket} Success!")
            except ClientError as e1:
                print(f"{fg('red')}Create new bucket {bucket} failed: {e1}{attr('reset')}")
                return False
            return True
        print(f"{fg('red')}The bucket {bucket} you have no access: {e}{attr('reset')}")
        return False
# print(check_bucket_permission("solutions-reference"))
print(check_bucket_permission("lin"))
# print(response.__dict__)
# my_bucket = s3.Bucket("lin")
# print(my_bucket.__dict__)
# for my_bucket_object in my_bucket.objects.all():
#     print(my_bucket_object)