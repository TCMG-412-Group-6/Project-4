#Andrew Dean
#TCMG 412 500 UIN - 230007137
#Program Title: Log Parser

#Functions
from threading import local
from urllib.request import urlretrieve
from datetime import date, datetime, timedelta
import os
import re

##Main Program

if not os.path.exists('log_copy.log'):
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    local_log = 'log_copy.log'
    print('Fetching Apache log file')
    # I liked this progress bar implementation, thanks for sharing!
    local_log, headers = urlretrieve(URL_PATH, local_log, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)
    print('Done!' )
    print('Created copy of log file named \'local_copy.log\' \nSaved at:', os.path.abspath(local_log), '\n')


##trying regex
#line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'
#regex = '\[(.{11}):(.{8}) (.*?)\] \"(.*?)\" (\d{3}) (\d+)'

sixmonths= 0
count= 0

##this takes a long time to run using regex, I wonder how I can cut it down?
sesame = open("log_copy.log", 'r')
for lines in sesame:
    parse = re.search(r'\[(.{11}):(.{8}) (.*?)\] \"(.*?)\" (\d{3}) (\d+)', lines)
    #parse.group(1)=date;
    #group(2)=time; 
    #group(3)=timezone - important for anything?; 
    #group(4)=everything in ""(need to parse it better);
    #group(5)=error codes!;
    #group(6)=whatever the end numbers mean;
    if parse:
        parsed_date = datetime.strptime(parse.group(1), '%d/%b/%Y').date()
    startdate = datetime(year=1995, month=4, day=12).date()
    if parsed_date >= startdate:
           sixmonths += 1
sesame.close()


##
counter = open("log_copy.log", "r")
content = counter.read()
numlines = content.split('\n')
for i in numlines:
    if i:
        count+=1
counter.close()
      
print("Total Requests Made 6 months starting April 11th, 1995 - Octobober 11th 1995: ", sixmonths)
print("Total Requests from the logfile: ", count)


