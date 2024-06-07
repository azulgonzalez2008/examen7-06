import requests
import json

response = requests.get('https://api.example.com/data')
if response.status_code == 200:
   
    print(response.json())
else:
    print(f'Error en la solicitud: {response.status_code}')
#error 
fetch('https://jsonplaceholder.typicode.com/posts')
  .then((response) => response.json())
  .then((json) => console.log(json));


