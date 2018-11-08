import json, requests

URL = 'http://localhost:8080/control_server/'

print('Get all control servers')
req_data = {
    'Action': 'GetControlServers',
}
r = requests.post(URL, data = req_data)
print(r.status_code, r.reason)
print(json.loads(r.text))

print('\nInsert control server')
req_data = {
    'Action': 'InsertControlServer',
    'Data': json.dumps({
        'IP': '127.0.0.1',
        'Port': '1',
        'Name': 'Test InsertControlServer'
    })
}
r = requests.post(URL, data = req_data)
print(r.status_code, r.reason)
print(json.loads(r.text))

print('\nUpdate control server')
json_resp = json.loads(r.text)
server = json_resp['Data']
req_data = {
    'Action': 'UpdateControlServer',
    'ID': server['id'],
    'Data': json.dumps({
        'IP': '127.0.0.2',
        'Port': '2',
        'Name': 'Test UpdateControlServer'
    })
}
r = requests.post(URL, data = req_data)
print(r.status_code, r.reason)
print(json.loads(r.text))

print('\nDelete control server')
json_resp = json.loads(r.text)
server = json_resp['Data']
req_data = {
    'Action': 'DeleteControlServer',
    'ID': server['id']
}
r = requests.post(URL, data = req_data)
print(r.status_code, r.reason)
print(json.loads(r.text))
