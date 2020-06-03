# 1st we need a way to talk HTTP
# We'll use the requests package that is very stable and widely used

# This is a standard py library - no need to install
import time

# Requests is not a standard library and must be installed with a package manager
# package is an external library of code, not native to python (or vanilla python)
# A package manager installs and manages this package

# Python, Ruby, JavaScript, Java; almost all modern languages have a package manager

import requests

# I want to make a get request to get more info on my postcode
# I need to check my API Documentation
# then build the target URK with patha nd args
# Then I need to use the package requests to make the request
# I will receive a JSON that I need to parse into a dictionary
path = 'http://api.postcodes.io/postcodes/'
args = 'bn246ay'

# build URL
url_target = path + args
print(url_target)

# time to request

response = requests.get(url_target)
print(response)
print(type(response))

# Parsing or getting dictionary out
print(response.json())
response_dictionary = response.json()
print(type(response_dictionary))
#
# for key in response_dictionary.keys():
#     print(key)
result_dictionary = response_dictionary['result']
for key in result_dictionary:
    print(key, ' IS ', result_dictionary[key])

print(result_dictionary['longitude'])
