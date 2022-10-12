import os
import boto3
import urllib.parse


def can_get_videos():
    try: 
        client_s3 = boto3.client('s3', 
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.environ.get("AWS_SECRET_KEY"))

        bucket = os.environ.get("AWS_SECURITY_BUCKET_NAME")
        curr_path = os.getcwd()
        response = client_s3.list_objects_v2(Bucket=bucket)
        files = response.get("Contents")

        for file in files:
            filename = os.path.join(curr_path, 'baseapp/static/videos', file['Key'])
            client_s3.download_file(
                Bucket=bucket,
                Key=file['Key'],
                Filename=filename
            )
        return True
    except:
        return False


def get_videos_formatted():
    vid_arr = []
    count = 0
    if can_get_videos():
        data_file_folder = os.path.join(os.getcwd(), 'baseapp/static/videos/')
        for file in os.listdir(data_file_folder):
            filepath = os.path.join(data_file_folder, file)
            with open(filepath, "r") as fp:
                fp.__setattr__('ns', file)
                fp.__setattr__('id', count)
                fp.__setattr__('urlpath', 'https://d37gl3wwe8ps5w.cloudfront.net/' + urllib.parse.quote(file))
                fp.__setattr__('date', file.split(' ')[0])
                vid_arr.insert(0, fp)
                count+=1
            os.remove(filepath)
    return vid_arr
    
def delete_video(id, key):
    print()

def main():
    get_videos_formatted()

    

if __name__ == "__main__":
    main()