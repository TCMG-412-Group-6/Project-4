#Logan K. MacDonald
#TCMG-412, Project 4
#Texas A&M University
#Spring 2022

from ast import Str
import re
import datetime
import os
from collections import Counter
# use os.path for file checking capability to check if log file has already been downloaded
from os.path import exists
import string
from tokenize import String
# use urlretrieve to retrieve log file after file check determined log had not already been downloaded
from urllib.request import urlretrieve



FILE_NAME = 'http_access_log.txt'

# check for log file prescence on system, if found use that file, if not retrieve from web
if not exists(FILE_NAME):
    print("Log file not found on system. Log file is being retrieved, please wait.")
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    LOCAL_FILE = 'http_access_log.txt'
    local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
    print("Done")

fh = open(FILE_NAME)

print("Stand By")

total_requests = 0
past_year_requests = 0
unsuccessful_requests_403 = 0
unsuccessful_requests_404 =0
unsuccessful_requests_4 =0
redirected_requests = 0
past_year = '/1995'
days = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
weeks = {}
months = {}
filenames = {}
files = {}

previous_month_file = ""
month_file = ""

with open("http_access_log.txt") as fh:
    Lines = fh.readlines()
    for line in Lines:
        #count total requests in log file
        total_requests += 1
        #count total requests in the past year in the log file
        if past_year in line:
            past_year_requests += 1
            #count the total number of unsuccesful 403 requests
            if "403 -" in line:
                unsuccessful_requests_403 += 1
            #count the total number of unsuccesful 404 requests
            if "404 -" in line:
                unsuccessful_requests_404 += 1
            #add 403 and 404 unsuccesful connection together to get the total
            unsuccessful_requests = unsuccessful_requests_403 + unsuccessful_requests_404
            #count the number of redirect 302 requests
            if "302 -" in line:
                redirected_requests += 1
        #Use RegEx to split the line and sort the data in the log
        result = re.split('.+ \[(.+) .+\] "[A-Z]{3,5} (.+) HTTP/1.0" ([0-9]{3})', line)
         # make sure the line is a proper request
        if len(result) == 5:
            date = result[1]
            file = result[2]
            
            # split the date and time, sort dates into dictionary
            date = date.split(':')
            if date[0] in days:
                days[date[0]] += 1
            else:
                days[date[0]] = 1
            
            # split day and month, sort months into dictionary    
            date[0] = date[0].split('/')
            if date[0][1] + " " + date[0][2] in months:
                months[date[0][1] + " " + date[0][2]] += 1
            else:
                months[date[0][1] + " " + date[0][2]] = 1
            
            # sort file names into dictionary
            if file in filenames:
                filenames[file] += 1
            else:
                filenames[file] = 1
        

print("total requests", total_requests)
print("past year requests", past_year_requests)
print("403", unsuccessful_requests_403)
print("404", unsuccessful_requests_404)
print("unsuccessful", unsuccessful_requests)
print("redirected", redirected_requests)

# printing the results
print("------------- Results -------------\n")
# number of past year and total requests
print("-----------------------------------")       
print("Total requests in the last year: " + str(past_year_requests))
print("Total requests in entire log: " + str(total_requests)iii)