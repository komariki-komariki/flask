import requests

# response = requests.post('http://127.0.0.1:5000/advertisement', json={'heading':'fjfjfjfj', 'description': 'jdjdjdj', 'owner': 'jgfjfgjf'},)
# response = requests.get('http://127.0.0.1:5000/advertisement/1')
response = requests.delete('http://127.0.0.1:5000/advertisement/1')
print(response.status_code)
print(response.text)
response = requests.get('http://127.0.0.1:5000/advertisement/1')
print(response.status_code)
print(response.text)