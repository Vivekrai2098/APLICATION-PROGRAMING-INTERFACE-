import requests
url='https://www.fast2sms.com/dev/bulkV2'
message=''
numbers=''
payload=f'sender_id=TXTIND&message={message}"&route=v3&numbers={numbers}'
headers={
    'authorization':'',
    'content-Type':'application/x-www-form-urlencoded'

}
response=requests.request('post',url=url,data=payload,headers=headers)
print(response.text)
