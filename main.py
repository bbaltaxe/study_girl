from botocore.vendored import requests 
import json
import csv
import time 
import boto3

# Make an http get request
request = requests.get('https://www.googleapis.com/youtube/v3/liveChat/messages?liveChatId=Cg0KC2hIVzFvWTI2a3hR&part=snippet&key=AIzaSyAA9XB1_C35bXonayY8SlPEG3ahUl9-BZw')

# Parse return text using json.loads function. Returns dict
response_dictionary = json.loads(request.text)

pubtime = "2018-11-07T23:28:07.290Z" #time of writing - arbitrarily low
runtime = time.time() + 60*1
waittime = 12 #seconds between polling

#make file and place stuff to it - doesn't add to existing file right now
with open('messages.txt','a+') as cfile:

    # run for 15 minutes only for preliminary testing data 
    while time.time() < runtime:
        print(str(time.time()) + ' now\n' + str(runtime) + ' end\n')    
        for event_dict in response_dictionary['items']:
            #print(json.dumps(event_dict['snippet'], indent=5));
       
            #don't rewrite something that has already been included! 
            if event_dict['snippet']['publishedAt'] > pubtime:
                cfile.write(event_dict['snippet']['publishedAt']+' '+ json.dumps(event_dict['snippet']['textMessageDetails']['messageText'], indent=5)+'\n')


                pubtime = event_dict['snippet']['publishedAt']

        time.sleep(waittime)

def lambda_handler(event, context):
    print(event)


