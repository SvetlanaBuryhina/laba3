import re
import time
import requests

html=open('meetup_api.html', 'w')
html.write('<!DOCTYPE html>\n')
html.write('<html><head><meta http-equiv="Content-Type" content="text/html" charset=UTF-8"></head><body><p>')
startTime=int(time.time())*1000
startDate=time.strftime("%d-%m-%Y %H:%M")
r=requests.get('https://api.meetup.com/2/concierge?key=7187f512f10195971732d4d2f4226a&sign=true&photo-host=public&country=us&city=Boston&category_id=34&state=MA')
address=re.findall(r'"address_1":"([\w\ \.\&]+)"', r.text)
names=re.findall(r'"name":"([\w\ \(\)\:]+)","id":"[\w ]+","time"', r.text)
len=len(names)
m=re.findall(r'"name":"[\w\ \(\)\:]+","id":"[\w ]+","time":([\d]+)', r.text)

html.write('<i> Today is ' + startDate + '</i>')
html.write('<p><b> Upcoming events: </b></p>')

for day in range(7):
    html.write(str(day+1) + ' day: \n<ul>\n')
    for i in range(len):
        if (int(m[i])<((day+1)*86400000+startTime)) and (int(m[i])>(day*86400000+startTime)):
            date=time.strftime("%a, %d-%m-%Y, %H:%M:%S", time.localtime(float(m[i])/1000))
            html.write('<li>' + "<b>Event: </b>'" + str(names[i]) + "'" + ', <b>Address: </b>' + str(address[i]) + ', <b>Date: </b>' + str(date) + '</li>\n')
    html.write('</ul>\n')
html.write('</p></body></html>')
