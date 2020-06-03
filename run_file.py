from another_get_request import *

path = 'http://api.postcodes.io/postcodes/'
exit_code = False
while not exit_code:
    postcode = input("Please enter your Postcode below: \n")

    if postcode.lower() == 'exit' or postcode.lower() == 'thank you, i am done for today':
        exit_code = True
    else:
        print(get_response(generate_URL(path, postcode)))
