# Sonnen-to-Influxdb2.0
Reads the Sonnenbatterie API and writes the data to influxdb2.0 

# Instructions:
1. Make sure you have influxdb2.0 and python3.9 installed
2. Download the file
3. Insert your Token, organisation and desired bucket (Influxdb)
4. Insert the port number of influxdb2.0 (I suggest running both on the same device)
5. Insert the correct ip adress of the Sonnenbatterie
5. Create a cron job (I suggest every 1 min)
6. Done

# Notes:
- It replaces the Systemstatus Ongrid with 1 and the Systemstatus OffGrid with 0 (for a better use in Grafana)
