import json
import requests

URL = 'http://localhost:8080/dashboard/'
ServerId = '5be329b0aabe5f9ca1f0a211'

print('Get all boards')
req_data = {
    'Action': 'GetBoards',
}
r = requests.post(URL, data = req_data)
print(r.status_code, r.reason)
print(json.loads(r.text))

print('\nInsert board')
req_data = {
    'Action': 'InsertBoard',
    'Data': json.dumps({
        'Serial': 'OSP-A2_005',
        'Server': ServerId,
        'Info': {
            'Hardware': {'PMD': '', 'CpuVersion': ''},
            'Software': {'CentOS': ''}
        },
        'Private': {
            'BMC': {'IP': '', 'Username': '', 'Password': '', 'MaxSOL': ''},
            'Power': {'Type': '', 'Vendor': '', 'IP': '', 'Port': ''}
        },
    })
}
r = requests.post(URL, data = req_data)
print(r.status_code, r.reason)
print(json.loads(r.text))

print('\nUpdate board')
board = json.loads(r.text)['Data']
req_data = {
    'Action': 'UpdateBoard',
    # 'ID': board['id'],
    'Serial': board['Serial'],
    'Data': json.dumps({
        'Info': {
            'Hardware': {'PMD': '920mV', 'CpuVersion': 'eMAG 2'},
            'Software': {'CentOS': '7.5'}
        },
        'Private': {
            'BMC': {'IP': '127.0.0.1', 'Username': 'ADMIN', 'Password': 'ADMIN', 'MaxSOL': '1'},
            'Power': {'Type': 'NPS', 'Vendor': 'NPS', 'IP': '127.0.0.1', 'Port': 'A0'}
        },
        'Devices': [
            {'Type': 'Memory', 'Vendor': 'Samsung', 'Capacity': '256GB', 'Speed': '2400Mhz'}
        ],
        'Note': {
            '2018-11-07': 'Re-work: installed U3',
            '2018-11-08': 'Test passed',
            '2018-11-09': 'Packed',
        }
    })
}
r = requests.post(URL, data = req_data)
print(r.status_code, r.reason)
print(json.loads(r.text))

print('\nDelete board')
board = json.loads(r.text)['Data']
req_data = {
    'Action': 'DeleteBoard',
    'ID': board['id']
}
r = requests.post(URL, data = req_data)
print(r.status_code, r.reason)
print(json.loads(r.text))
