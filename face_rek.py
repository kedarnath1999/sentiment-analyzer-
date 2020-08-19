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

photo = 'face_pic.jpg'

client = boto3.client('rekognition',aws_access_key_id=access_key_id,
                       aws_secret_access_key=secret_access_key,region_name='us-east-2')

with open(photo,'rb') as source_img:#rb is binary mode
    source_bytes = source_img.read()
response = client.detect_faces(
    Image={
        'Bytes': source_bytes
    },
    Attributes=[
        'ALL',
    ])
#print(response)
for i in response['FaceDetails']:
    print(i)
    print('-----------------------------------------------------------------------------------------------------')


