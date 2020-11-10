import os
import requests
import polling
import time
import calendar
import math
import xml.etree.ElementTree as ET
#from dotenv import load_dotenv

R = 6372.795477598

load_dotenv(verbose=True)

doa_server_addr = os.getenv('DOA_SERVER_ADDR')
#spaciallite_server_addr = os.getenv('SPACIALLITE_SERVER_ADDR')
def do_process():
    try:
        response = requests.get(doa_server_addr)
        response.raise_for_status()

        #print('Received data...', response.text)
        
        doa_value = 0.0
        conf_value = 0.0
        pwr_value = 0.0

        for child in ET.fromstring(response.text):
            if child.tag.lower() == 'doa':
                doa_value = float(child.text)
            if child.tag.lower() == 'conf':
                conf_value = int(child.text)
            if child.tag.lower() == 'pwr':
                pwr_value = float(child.text)
        
        data = [doa_value, conf_value, pwr_value]
        post_data = {'doa value': doa_value,
                    'conf value: ': conf_value,
                    'pwr value: ':  pwr_value}
        
        #print(post_data)
        
    
        #TODO: make a writer 
        #response = request.post(spaciallite_server_addr, data = post_data)
        #response.raise_for_status()

        #print('Sent data... ', post_data)

    except requests.exceptions.Timeout as err:
        print(err)
    except requests.exceptions.TooManyRedirects as err:
        print(err)
    except requests.exceptions.HTTPError as err:
        print(err)
    except requests.exceptions.RequestException as err:
        print(err)
    except ET.ParseError as err:
        print(err)
        
    return (data)
        
def main():    
    do_process()
    
if __name__ == '__main__':
    main()