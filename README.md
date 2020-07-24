# meraki-read-devices
A python script to read device data from the Meraki API.

This script:
- Reads data from an ini file which contains customer specific information plus details of which device data is required.
- Connects to the Meraki API using the REST API.
- Downloads device data.
- Converts it to JSON (the data is a list containing multiple dictionaries)
- Places it in a Pandas dataframe.
- Drops columns containing unwanted device data.
- Saves it to a CSV file. The name of the CSV file includes the customer, date and time.

Multiple ini files are supported - the user enters the name of the ini file to be used when the program runs.

 ## Module Requirements
 This script requires the following modules to be imported:
 - requests
 - pandas
 
 These can be imported using *pip install requests* and *pip install pandas*
 
 Alternately you can install all dependencies using *pip install -r requirements.txt*
 
 ## Populating the ini File
 Replace the *???* placeholders in the ini file with the relevant values for the customer and network that you are gathering device data for.
 
 For column data that you want included in the CSV file set the relevant value to *include*. For columns that you do not want set the relevant value to *drop*.
 
 ```
 [MERAKI]
api_key = ???

[CUSTOMER]
customername = ???
organization = ???
network = ???

[COLUMNS]
lat = drop
lng = drop
address = drop
serial = include
mac = include
lanIp = include
tags = drop
url = drop
networkId = include
name = include
model = include
firmware = include
floorPlanId = include
switchProfileId = include
 ```
