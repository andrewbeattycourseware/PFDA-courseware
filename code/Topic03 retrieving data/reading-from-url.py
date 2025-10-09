# A program to demonstrate getting data from the web using the requests opject
# Author: Andrew Beatty

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print (data)
# we can now analye the data
for event in data["northern-ireland"]["events"]:
    #print (f"{event}")
    print (f"{event['title']} on {event['date']}")


url = "https://drive.google.com/uc?id=1phaHg9objxK2MwaZmSUZAKQ8kVqlgng4&export=download"
response = requests.get(url)
print (response.text)
