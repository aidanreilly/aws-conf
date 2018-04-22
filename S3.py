import boto3
import config

class S3Controller:

    # A class for controlling interactions with amazon's S3 storage service.

    def __init__(self):
        pass

    def list_buckets( self, s3 ):

        # Print out a list of all s3 buckets your credentials have created,
        # using Resource "s3"

        for bucket in s3.buckets.all():
            print( bucket )

    def create_bucket( self, s3, bucket_name ):

        # Create and return an S3 bucket with name "bucket_name"
        # using "s3" Resource
        
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
            "LocationConstraint":"eu-west-1"})
        return s3.Bucket( bucket_name )

    def delete_bucket(self, s3, bucket_name):

        # Delete the S3 bucket with name "bucket_name"
        # using the "s3" Resource

        bucket = s3.Bucket(bucket_name)
        #must delete all objects/keys before you can delete bucket
        for key in bucket.objects.all():
            key.delete()   
        bucket.delete()
    

    def upload_file(self, s3, bucket_name, file_name, key ):

        # Upload the file "file_name" to S3 storage, into the bucket
        # "bucket_name", using the "s3" Resource. The name 'key' will
        # be used to reference the file in the S3 Storage.

        bucket = s3.Bucket(bucket_name)
        bucket.upload_file( file_name, key )

    def download_file(self, s3, bucket_name, key, local_file_name ):

        # Download the file referenced by 'key',  in the S3 bucket with
        # name "bucket_name", to the file location "local_file_name"
        # using the "s3" Resource

        s3.Bucket(bucket_name).download_file( key, local_file_name )

    def delete_file(self, s3, bucket_name, key):

        client = boto3.client('s3')
        client.delete_object(Bucket=bucket_name, Key=key)
 
    def list_objects(self, s3, bucket_name):
        bucket = s3.Bucket(bucket_name)
        for object in bucket.objects.all():
            print(object)