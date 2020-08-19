import csv
import boto3

with open('new_user_credentials.csv') as input:
    next(input) ## to read input from next line
    reader = csv.reader(input)
    for line in reader:
        access_key_id = line[2]
        secret_access_key = line[3]
    #print(access_key_id)
    #print(secret_access_key)

photo = 'virat.jpg'
target_photo = 'team.jpg'

client = boto3.client('rekognition',aws_access_key_id=access_key_id,
                       aws_secret_access_key=secret_access_key,region_name='us-east-2')

with open(photo,'rb') as source_img:#rb is binary mode
    source_bytes = source_img.read()

with open(target_photo,'rb') as target_img:#rb is binary mode
    target_bytes = target_img.read()


response = client.compare_faces(
    SourceImage={
        'Bytes': source_bytes
    },
    TargetImage={
        'Bytes': target_bytes
    }
    )
print(response)



