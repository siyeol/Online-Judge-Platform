from urllib import response
import requests
import argparse
import json

parser = argparse.ArgumentParser(description='Test for modules')
parser.add_argument('--module', type=str, help='add module you want to test')


url = "http://localhost:80/code_run/"
sub_url = parser.parse_args().module
# url+=sub_url

my_str = """
def minus(a, b):
    return (a-b)

a, b = 2, 3
result = minus(a, b)
print(result)
"""

# print((json_data))
response = requests.post(url, json={"code" : my_str, "class_id": 0, "assign_id": 1, "user_id": 35520})
print (response.json())

assert response.status_code == 200

print('\x1b[6;30;42m' + 'SUCCESS!' + '\x1b[0m')