"""
Discover how to retrieve, send, and process data, and make your applications 
dynamic and responsive.
"""

"""
Status code meaning: 
200 OK
404 NOT FOUND
505 INTERNAL SERVER ERROR
"""

import requests

# api key: 
url = 'http://www.omdbapi.com/?apikey=e6642a56&'
# Get requrests

request_statement = f"{url}s=fast"
response =  requests.get(request_statement)
data = response.json()
print(response.status_code)
print(data)
print(request_statement)


#Declare a function 
"""
def function takes in :
- title name 
- type : Default is none
- year : Default is none

This function is for formatting the API requrest statement
"""

def requrest_statement_formatter(title_name: str, type = None, year = None):
    pass