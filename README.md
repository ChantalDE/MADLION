# MADLION
Imports data from kerberoSDR and uploads it to Geoserver on a map through postgreSQL DB.
This is not a working implementation yet.

2 separate repositories should be created. Right now it is just displayed in folders as 'server' and 'input data KSDR'.
These folders contain the scripts that are needed for pi and the server to communicate and calculate and plot the location of an IOT device at a certain frequency.

In the server
- the data is being processed through calculations.py (from triangulation.py in https://github.com/sofwerx/synthetic-target-triangulator)
- This Geojson output will be translated to XML where the point will be plotted and stored through Geoserver(sendLayer.js, from https://github.com/SKalt/geojson-to-wfs-t-2)
- the driver is supposed to retrieve the correct information of the correlating 3 points to proccess.

In the machine
- The data is being retrieved by receive_lob.py (from https://github.com/rtlsdrblog/pyRDFMapper-KSDR-Adapter)
- the main program syncs to the frequency of the target, and sends the data to the dataBase

instalment requirements in server:
- psycopg2 (instalment link: https://www.psycopg.org/docs/install.html)
- https://github.com/SKalt/geojson-to-wfs-t-2 (js)
- express (js)
- xmlhttprequest

instalment requirements in machine:
- xml.etree
- instead of getLob.py use RDFMapper, and change the serveriP in the environment. (link: https://github.com/rtlsdrblog/pyRDFMapper-KSDR-Adapter)
- psycopg2 (instalment link: https://www.psycopg.org/docs/install.html)

TODO:
- Write correct queries to sync the machines to the same target, and switch between targets. Switch every x seconds
- Write correct queries to retrieve correct 3 points systematically, and store those outputs in variables. Some of these variables will be used in an object of the targetLock class that will locate the point that will be posted. The 'metadata' variables will be placed directly in the Geojson format.





