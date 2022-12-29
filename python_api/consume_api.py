import requests
import json


api_link = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow'

response = requests.get(api_link)

for question in response.json()['items']:
    if question['answer_count'] == 0 :
        print(question['title'])
        print(question['link'])
        print(question['is_answered'])
    else:
        print('skipped')
    print()
# print(response.json()['items'])



