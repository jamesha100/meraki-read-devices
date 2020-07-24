import requests
import datetime
import pandas as pd
import pprint
from configparser import ConfigParser

########################################################################################################################

def main():
    # Import values for the customer environment from ini file using ConfigParser

    inifile = input('Enter the name of the customer ini file: ')
    config = ConfigParser()
    config.read(inifile)

    customername = config.get('CUSTOMER', 'customername')
    organization = config.get('CUSTOMER', 'organization')
    network = config.get('CUSTOMER', 'network')
    api_key = config.get('MERAKI', 'api_key')
    print()
    print('Customer name is: ', customername)
    print()
    print('Organization is: ', organization)
    print()
    print('Network is: ', network)
    print()
    print('API Key is: ', api_key)
    print()

    # Read COLUMNS section from ini file to dictionary
    columns_dict = dict(config['COLUMNS'])

    print(columns_dict)

    # Create url using organization and network values read from ini file
    url = url = f'https://api.meraki.com/api/v0/organizations/{organization}/networks/{network}/devices'

    print(url)
    payload = {}
    # Create headers using api key read from ini file

    headers = {'X-Cisco-Meraki-API-Key': api_key}

    # Make API request to Meraki
    response = requests.request("GET", url, headers=headers, data=payload)

    # Check for correct API reponse
    if response.status_code != 200:
        raise Exception(f'HTTP response was {response.status_code}, and 200 was expected. ' +
                        'Please ensure your Meraki API Value, organization and network are correct.')
    else:
        # Convert API response to JSON object
        devices_json = response.json()

    pprint.pprint(devices_json)

    # Create Pandas dataframe using JSON data
    device_df = pd.DataFrame(devices_json)

    print(device_df)

    # Drop unwanted columns from dataframe
    for key in columns_dict:
        print(key, columns_dict[key])
        if columns_dict[key] == 'drop':
            device_df.drop(key, axis=1, inplace=True)


    # Create filename for output file

    now = datetime.datetime.now()
    outputfile = customername + '-devices-' + now.strftime("%Y-%m-%d-%H-%M-%S") + '.csv'

    # Write dataframe to csv
    device_df.to_csv(outputfile, index = False)
    print (f'The device information has been stored in {outputfile}')




########################################################################################################################

if __name__ == "__main__":
    main()
