import math
import speedtest
import pygal

def bytes_to_mb(size_bytes):
    i=int(math.floor(math.log(size_bytes,1024)))
    power=math.pow(1024,i)
    size=round(size_bytes/power,2)
    return f"{size}"

wifi=speedtest.Speedtest()
print('Getting Download Speed...')
download_speed=wifi.download()
a=bytes_to_mb(download_speed)
download_speed=int(float(a))

wifi.upload(pre_allocate=False)
print("Getting Upload Speed...")
upload_speed=wifi.upload()
b=bytes_to_mb(upload_speed)
upload_speed=int(float(b))

print("Download: ",download_speed)
print("Upload: ",upload_speed)

# creating the chart object 
Solid_Gauge = pygal.SolidGauge(inner_radius = 0.75,half_pie = True)  

# naming the title 
Solid_Gauge.title = 'Internet Speed Test'	
# Random data

Solid_Gauge.add('Upload Speed', [{'value': download_speed, 'max_value': 100}]) 
Solid_Gauge.add('Download Speed', [{'value': upload_speed, 'max_value': 100}])  
Solid_Gauge.render_to_file('speed_test.png')
