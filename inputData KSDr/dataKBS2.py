import psycopg2

#from receive_lob import do_process

#data = do_process()

#doa_value = data[0]
#conf_value = data[1]
#pwr_value = data[2]
#lat = data[3]
#lon = data[4]

#test hardcoded values
name = 'KBS2'
angle = 38.17583333
lat = 27.956774
lon = -82.436587
conf_value = 2
pwr_value = 3

try:
   connection = psycopg2.connect(user="geoserver", password="abc", host="3.22.118.224", port="5432", dbname="shapes")
   cursor = connection.cursor()

   postgres_insert_query = """ INSERT INTO points(long, lat, angle, name, conf_value, pwr_value) VALUES (%s,%s,%s,%s,%s,%s)"""
   record_to_insert = (lon, lat, angle, name, conf_value, pwr_value)
   cursor.execute(postgres_insert_query, record_to_insert)

   connection.commit()
   count = cursor.rowcount
   print (count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")