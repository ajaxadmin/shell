import requests
url = "https://app.cloudcone.com/ajax/compute"
dic = {
    'cookie': 'CCM19=p0itslq2ip84eds3an4un5n8c0; _ga=GA1.2.1018913389.1649594834; _fbp=fb.1.1649594834528.102006057; __stripe_mid=b75d743d-e01f-4992-aad1-429a04a2fe5ead0688; crisp-client%2Fsession%2Fb4a6582f-f407-4054-b73c-d6e4bf698b1e=session_e485b8c5-7ba2-4098-bc19-e046291fee7d; crisp-client%2Fsession%2Fb4a6582f-f407-4054-b73c-d6e4bf698b1e%2F02b0d4abe469cbac41988da7d0657fd798bb86f787203c4b526b9a7043dbf8a8=session_e485b8c5-7ba2-4098-bc19-e046291fee7d; redirect=%2Fbilling; tz=Asia/Shanghai; _gid=GA1.2.33314784.1649734833',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36",
    # 'text': '测试提交'
}
dat = {
    'cpu': '1',
    'ram': '2048',
    'disk': '40',
    'ips': '1',
    'os': '423',
    'hostname': '123.123',
    'plan': '244',
    'method': 'provision',
    '_token': 'fOrhS9c8',
}
cook = {
    'cookie': 'CCM19=p0itslq2ip84eds3an4un5n8c0; _ga=GA1.2.1018913389.1649594834; _fbp=fb.1.1649594834528.102006057; __stripe_mid=b75d743d-e01f-4992-aad1-429a04a2fe5ead0688; crisp-client%2Fsession%2Fb4a6582f-f407-4054-b73c-d6e4bf698b1e=session_e485b8c5-7ba2-4098-bc19-e046291fee7d; crisp-client%2Fsession%2Fb4a6582f-f407-4054-b73c-d6e4bf698b1e%2F02b0d4abe469cbac41988da7d0657fd798bb86f787203c4b526b9a7043dbf8a8=session_e485b8c5-7ba2-4098-bc19-e046291fee7d; redirect=%2Fbilling; tz=Asia/Shanghai; _gid=GA1.2.33314784.1649734833'
}
proxies = {"http": "http://127.0.0.1:10808", "https": "http://127.0.0.1:10808"}
resp = requests.post(url=url, headers=dic, cookies=cook, data=dat)
resp.close()
print(resp.text)
