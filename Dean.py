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

#this skips the process of redownloading the log file if it already exists in the directory.
#for whatever reason, it doesn't want to save the log file inside the local github repo - 
#instead it saves the file one directory up (for me)
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
#regex = '\[(.{11}):(.{8}) (?:.*?)\] \"(?:.{3}) (.*?) (?:.*?)\" (\d{3}) (\d+)'

sixmonths= 0
count= 0

##this takes a long time to run using regex, I wonder how I can cut it down?
sesame = open("log_copy.log", 'r')
for lines in sesame:
    parse = re.search(r'\[(.{11}):(.{8}) (?:.*?)\] \"(?:.{3}) (.*?) (?:.*?)\" (\d{3}) (\d+)', lines)
    #parse.group(1)=date; <--
    #parse.group(2)=time; 
    #parse.group(3)=filename+file extension <--
    #parse.group(4)=error codes!; <--
    #parse.group(5)=whatever the end numbers mean; (not sure if important?)
    if parse:
        parsed_date = datetime.strptime(parse.group(1), '%d/%b/%Y').date()
        parsed_time = datetime.strptime(parse.group(2), '%H:%M:%S').time()
        parsed_filename = parse.group(3)
        parsed_code = parse.group(4)
## There absolutely has to be a better way to sort and iterate the monthly logs
## The repeat execution protection I tried to implement breaks the writing process - only 1 entry per file, so commented out for now.
    #if not os.path.exists('1 Jan log.log'):
        if datetime(year=1995, month=1, day=1).date() <= parsed_date < datetime(year=1995, month=2, day=1).date():
            f = open('1 Jan log.log', 'a')
            f.write(lines)
    #if not os.path.exists('2 Feb log.log'):
        if datetime(year=1995, month=2, day=1).date() <= parsed_date < datetime(year=1995, month=3, day=1).date():
            f = open('2 Feb log.log', 'a')
            f.write(lines)
    #if not os.path.exists('3 Mar log.log'):
        if datetime(year=1995, month=3, day=1).date() <= parsed_date < datetime(year=1995, month=4, day=1).date():
            f = open('3 Mar log.log', 'a')
            f.write(lines)
    #if not os.path.exists('4 Apr log.log'):
        if datetime(year=1995, month=4, day=1).date() <= parsed_date < datetime(year=1995, month=5, day=1).date():
            f = open('4 Apr log.log', 'a')
            f.write(lines)
    #if not os.path.exists('5 May log.log'):
        if datetime(year=1995, month=5, day=1).date() <= parsed_date < datetime(year=1995, month=6, day=1).date():
            f = open('5 May log.log', 'a')
            f.write(lines)
    #if not os.path.exists('6 Jun log.log'):
        if datetime(year=1995, month=6, day=1).date() <= parsed_date < datetime(year=1995, month=7, day=1).date():
            f = open('6 Jun log.log', 'a')
            f.write(lines)
    #if not os.path.exists('7 Jul log.log'):
        if datetime(year=1995, month=7, day=1).date() <= parsed_date < datetime(year=1995, month=8, day=1).date():
            f = open('7 Jul log.log', 'a')
            f.write(lines)
    #if not os.path.exists('8 Aug log.log'):
        if datetime(year=1995, month=8, day=1).date() <= parsed_date < datetime(year=1995, month=9, day=1).date():
            f = open('8 Aug log.log', 'a')
            f.write(lines)
    #if not os.path.exists('9 Sep log.log'):
        if datetime(year=1995, month=9, day=1).date() <= parsed_date < datetime(year=1995, month=10, day=1).date():
            f = open('9 Sep log.log', 'a')
            f.write(lines)
    #if not os.path.exists('10 Oct log.log'):
        if datetime(year=1995, month=10, day=1).date() <= parsed_date < datetime(year=1995, month=11, day=1).date():
            f = open('10 Oct log.log', 'a')
            f.write(lines)
    
    
##this bit is just testing the new methods applied to the first group project    
    startdate = datetime(year=1995, month=4, day=12).date()
    if parsed_date >= startdate:
           sixmonths += 1
sesame.close()


##can safely ignore this
counter = open("log_copy.log", "r")
content = counter.read()
numlines = content.split('\n')
for i in numlines:
    if i:
        count+=1
counter.close()
      
print("Total Requests Made 6 months starting April 11th, 1995 - Octobober 11th 1995: ", sixmonths)
print("Total Requests from the logfile: ", count)


