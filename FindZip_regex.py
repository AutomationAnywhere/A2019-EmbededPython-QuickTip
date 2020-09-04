import re

def findZip(address):
    postal_code = re.search('\d{5}(-\d{4})?', address)
    try:
        zip = address[postal_code.span()[0]:postal_code.span()[1]]
    except:
        zip = "Could not find match in provided string"
    return zip

#To test directly in python...dont copy this line or the lines below to the Automation Anywhere JavaScript Action
address = "Some random text Dayton, OH 45459-3321 Then some other random text"
print(findZip(address))