from calendar import month
import requests 
from datetime import datetime

TOKEN ='h324aslkdf241askjd' 
username = 'thanosapollo'
running_graph = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'


user_params = {
    'token' : 'h324aslkdf241askjd',
    'username' : 'thanosapollo',
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes',

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

graph_config = {
    'id' : 'graph1',
    'name' : 'running',
    'unit' : 'Km',
    'type': 'float',
    'color' : 'sora'
}

headers = {
    'X-USER-TOKEN' : f'{TOKEN}'
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()
print(today.strftime('%Y%m%d'))


pixel_creation_endpoint = f'{pixela_endpoint}/{username}/graphs/{running_graph}'
pixel_creation_params = {
    'date' : today.strftime('%Y%m%d'),
    'quantity' : '4.20'
}





response = requests.post(url= pixel_creation_endpoint, json=pixel_creation_params, headers=headers)
print(response)
