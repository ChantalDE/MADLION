import psycopg2
import json
import requests
from calculations import TargetLoc



# def getMobileDetails(mobileID):
#     try:
#         connection = psycopg2.connect(user="geoserver", password="abc", host="3.22.118.224", port="5432", dbname="shapes")

#         print("Using Python variable in PostgreSQL select Query")
#         cursor = connection.cursor()
#         postgreSQL_select_Query = "select * from mobile where id = %s"

#         cursor.execute(postgreSQL_select_Query)
#         mobile_records = cursor.fetchall()
#         for row in mobile_records:
#             print("long = ", row[0], )
#             print("lat = ", row[1])
#             print("angle  = ", row[2])

#     except (Exception, psycopg2.Error) as error:
#         print("Error fetching data from PostgreSQL table", error)

#     finally:
#         # closing database connection
#         if (connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed \n")

# getMobileDetails(2)
# getMobileDetails(3)






sofTest = {"coords": [{"lat": 27.957261, "lon": -82.436587, "aob": 494.91444444, "angleUnit": "deg"}, {"lat": 27.956774, "lon": -82.436587, "aob": -321.8241667, "angleUnit": "deg"}, {"lat": 27.957050, "lon": -82.435950, "aob": 269.50611111, "angleUnit": "deg"}]}
t = TargetLoc()

#print(sofTest)
target = t.locate(sofTest)
print(target)

hasIntersect = target['hasIntersect']
targetLoc = target['targetLoc']
lat = targetLoc['lat']
lon = targetLoc['lon']



test = {
    "type": "FeatureCollection",
    "features": [
        {
            "type": "Feature",
            "properties": {
              "lon": lon,
              "lat": lat
            },
            "geometry": {
                "type": "Point",
                "coordinates": [
                    lat,
                    lon
                ]
            }
        }
    ]
}
jsont = json.dumps(test, indent=4)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url ='http://localhost:3000/', data = jsont, headers = headers)
#r = requests.get(url ='http://localhost:3000')
print(r.text)




