from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json
import urllib.request

# You can generate an API token from the "API Tokens Tab" in the UI
token = "XXX"
org = "XXX"
bucket = "XXX"

#gets a dictionary fromt he request
data = urllib.request.urlopen("http://192.168.0.XXX:8080/api/v1/status").read()
request = json.loads(data)
#remove date (is already given)
request.pop('Timestamp')
#sqeuence containing the elements
sequence = []
for key, value in request.items():
    if key == 'SystemStatus':
        if value == 'OnGrid':
            sequence.append("mem,host=host1 "+str(key)+"=1")
        else:
            sequence.append("mem,host=host1 "+str(key)+"=0")
    else:
        sequence.append("mem,host=host1 "+str(key)+"="+str(value))


with InfluxDBClient(url="http://127.0.0.1:XXX", token=token, org=org) as client:
    write_api = client.write_api(write_options=SYNCHRONOUS)
    write_api.write(bucket, org, sequence)


client.close()
