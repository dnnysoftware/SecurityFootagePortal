import os
import boto3
import urllib.parse
from django import forms
from django.db import models
from django.forms import ModelForm

class VideoSearch(models.Model):
    date = models.CharField(max_length = 10)

class VideoSearchForm(ModelForm):
    class Meta:
        model = VideoSearch
        fields = ('date',)


def get_videos():
    try: 
        client_s3 = boto3.client('s3', 
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_KEY"))

        bucket = os.environ.get("AWS_SECURITY_BUCKET_NAME")
        response = client_s3.list_objects_v2(Bucket=bucket)
        return response.get("Contents")
    except:
        return None


def get_videos_formatted():
    vids = get_videos()
    count = 0
    if vids != None:
        for file in vids:
            file['ns'] = file['Key']
            file['date'] = file['ns'].split(' ')[0]
            file['id'] = count
            file['urlpath'] = 'https://d37gl3wwe8ps5w.cloudfront.net/' + urllib.parse.quote(file['Key'])
            count+=1
    return vids
    
def delete_video(id, key):
    print()

def main():
    get_videos_formatted()

    

if __name__ == "__main__":
    main()