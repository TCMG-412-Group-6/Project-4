#Andrew Dean
#TCMG 412 500
#Program Title: Log Parser 2: Electric Boogaloo

#Functions
from threading import local
from urllib.request import urlretrieve
from datetime import date, datetime, timedelta
from os.path import abspath, exists
import re

##Main Program

#this skips the process of redownloading the log file if it already exists in the directory.
if not exists('log_copy.log'):
    URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    local_log = 'log_copy.log'
    print('Fetching Apache log file')
    # I liked this progress bar implementation, thanks for sharing!
    local_log, headers = urlretrieve(URL_PATH, local_log, lambda x,y,z: print('.', end='', flush=True) if x % 100 == 0 else False)
    print('Done!' )
    print('Created copy of log file named \'local_copy.log\' \nSaved at:', abspath(local_log), '\n')


##trying regex
#line = 'local - - [24/Oct/1994:13:41:41 -0600] "GET index.html HTTP/1.0" 200 150'
regex = re.compile('(?:.*?) - - \[(.{11})(?:.*?)\] \"(?:.{3}) (.*?) (?:.*?)\" (\d{3}) (?:.+)')
#(?:arg) means non-capture group

ERRORS= []
parse=[]
dates = {}
codes = {}
files = {}
sixmonths= 0
total_count= 0
months={}

print('Parsing log file, this may take a few moments... \n')
##this takes a long time to run using regex, I wonder how I can cut it down? 
for lines in open("log_copy.log", 'r'):
    total_count+= 1
    parse = regex.split(lines) 
    #parse[0]= was supposed to be full line; (this isn't currently working, and I'm not sure why -- parse[0] is an empty string)
    #parse[1]=date; <--
    #parse[2]=filename+file extension <--
    #parse[3]=error codes!; <--
    #parse[4] = '\n' and I'm not sure why, as I don't think my regex is set to capture it
    if not parse or len(parse) < 3:
        ERRORS.append(lines)
        continue
    parsed_date = datetime.strptime(parse[1], '%d/%b/%Y').date()
    parsed_filename = parse[2]
    parsed_code = parse[3]

    #Since the log files start in Oct 1994 rather than Jan 1995,
    #Trying this in order to bypass the problem of combining Oct thru Dec 1994 with 1995 results
    cut_date = datetime.strftime(parsed_date, '%b %Y')
    if cut_date in months:
        months[cut_date]+=1
    else:
        months[cut_date]=1

    if parsed_date in dates:
        dates[parsed_date]+=1
    else:
        dates[parsed_date]=1

    if parsed_filename in files:
        files[parsed_filename]+=1
    else:
        files[parsed_filename]=1

    if parsed_code in codes:
        codes[parsed_code]+=1
    else:
        codes[parsed_code]=1

##this bit is just testing the new methods applied to the first group project    
    startdate = datetime(year=1995, month=4, day=12).date()
    if parsed_date >= startdate:
        sixmonths += 1



## There absolutelly has to be a better way to sort and iterate the monthly logs
## I would ideally like there to be protection against doing this each time the program is executed

    #if datetime(year=1994, month=10, day=1).date() <= parsed_date < datetime(year=1994, month=11, day=1).date():
        #f = open('1 Oct 1994.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1994, month=11, day=1).date() <= parsed_date < datetime(year=1994, month=12, day=1).date():
        #f = open('2 Nov 1994.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1994, month=12, day=1).date() <= parsed_date < datetime(year=1995, month=1, day=1).date():
        #f = open('3 Dec 1994.log', 'w')
        #f.write(lines,'\n')        

    #if datetime(year=1995, month=1, day=1).date() <= parsed_date < datetime(year=1995, month=2, day=1).date():
        #f = open('4 Jan log.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1995, month=2, day=1).date() <= parsed_date < datetime(year=1995, month=3, day=1).date():
        #f = open('5 Feb log.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1995, month=3, day=1).date() <= parsed_date < datetime(year=1995, month=4, day=1).date():
        #f = open('6 Mar log.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1995, month=4, day=1).date() <= parsed_date < datetime(year=1995, month=5, day=1).date():
        #f = open('7 Apr log.log', 'w')
         #f.write(lines,'\n')

    #if datetime(year=1995, month=5, day=1).date() <= parsed_date < datetime(year=1995, month=6, day=1).date():
        #f = open('8 May log.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1995, month=6, day=1).date() <= parsed_date < datetime(year=1995, month=7, day=1).date():
        #f = open('9 Jun 1995 log.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1995, month=7, day=1).date() <= parsed_date < datetime(year=1995, month=8, day=1).date():
        #f = open('10 Jul log.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1995, month=8, day=1).date() <= parsed_date < datetime(year=1995, month=9, day=1).date():
        #f = open('11 Aug 1995 log.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1995, month=9, day=1).date() <= parsed_date < datetime(year=1995, month=10, day=1).date():
        #f = open('12 Sep 1995 log.log', 'w')
        #f.write(lines,'\n')

    #if datetime(year=1995, month=10, day=1).date() <= parsed_date < datetime(year=1995, month=11, day=1).date():
        #f = open('13 Oct log.log', 'w')
        #f.write(lines,'\n')
    
top_file = max(files, key=files.get)
top_file_value = max(files.values())
bottom_file = min(files, key=files.get)
bottom_file_value = min(files.values())
total_fails = codes['400'] + codes['401'] + codes['403'] + codes['404']
total_redi = codes['302'] + codes['304']
percent_fail = float(total_fails)/float(total_count) * 100
percent_redi = float(total_redi)/float(total_count) * 100


print("Total Requests Made 6 months starting April 11th, 1995 - Octobober 11th 1995: ", sixmonths)
print("Total Requests from the logfile: ", total_count,'\n')
print("Requests made by month:\n",months,"\n")
#print(codes)
print("Total Requests that ended in Failure codes:", total_fails)
print("Percentage of Requests that failed:", percent_fail,'%\n')
print("Total Requests that ended in Redirects:", total_redi)
print("Percentage of Requests that redirected:", percent_redi,'%\n')
print('Top requested file:',top_file,'with',top_file_value,'requests')
print('Least requested file:',bottom_file,'with',bottom_file_value,'requests')



