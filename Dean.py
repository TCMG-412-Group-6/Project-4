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
#these lists hold each line separated by datetime sorting
log1=[]
log2=[]
log3=[]
log4=[]
log5=[]
log6=[]
log7=[]
log8=[]
log9=[]
log10=[]
log11=[]
log12=[]
log13=[]

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
    #adds counts to number of requests by day
    if parsed_date in dates:
        dates[parsed_date]+=1
    else:
        dates[parsed_date]=1
    #adds counts to each filename
    if parsed_filename in files:
        files[parsed_filename]+=1
    else:
        files[parsed_filename]=1
    #adds counts to each error code
    if parsed_code in codes:
        codes[parsed_code]+=1
    else:
        codes[parsed_code]=1

##this bit is just testing the new methods applied to the first group project    
    startdate = datetime(year=1995, month=4, day=12).date()
    if parsed_date >= startdate:
        sixmonths += 1
## There absolutely has to be a better way to sort and iterate the monthly logs. This works, but slows down the parse considerably.
## if parse[0] was capturing the full string, this wouldn't be an issue and I could do it outside of the loop.
    if datetime(year=1994, month=10, day=1).date() <= parsed_date < datetime(year=1994, month=11, day=1).date():
        log1.append(lines)
    if datetime(year=1994, month=11, day=1).date() <= parsed_date < datetime(year=1994, month=12, day=1).date():
        log2.append(lines)
    if datetime(year=1994, month=12, day=1).date() <= parsed_date < datetime(year=1995, month=1, day=1).date():
        log3.append(lines)        
    if datetime(year=1995, month=1, day=1).date() <= parsed_date < datetime(year=1995, month=2, day=1).date():
        log4.append(lines)
    if datetime(year=1995, month=2, day=1).date() <= parsed_date < datetime(year=1995, month=3, day=1).date():
        log5.append(lines)
    if datetime(year=1995, month=3, day=1).date() <= parsed_date < datetime(year=1995, month=4, day=1).date():
        log6.append(lines)
    if datetime(year=1995, month=4, day=1).date() <= parsed_date < datetime(year=1995, month=5, day=1).date():
        log7.append(lines)
    if datetime(year=1995, month=5, day=1).date() <= parsed_date < datetime(year=1995, month=6, day=1).date():
        log8.append(lines)
    if datetime(year=1995, month=6, day=1).date() <= parsed_date < datetime(year=1995, month=7, day=1).date():
        log9.append(lines)
    if datetime(year=1995, month=7, day=1).date() <= parsed_date < datetime(year=1995, month=8, day=1).date():
        log10.append(lines)
    if datetime(year=1995, month=8, day=1).date() <= parsed_date < datetime(year=1995, month=9, day=1).date():
        log11.append(lines)
    if datetime(year=1995, month=9, day=1).date() <= parsed_date < datetime(year=1995, month=10, day=1).date():
        log12.append(lines)
    if datetime(year=1995, month=10, day=1).date() <= parsed_date < datetime(year=1995, month=11, day=1).date():
        log13.append(lines)

#repeat protection against re-writing separated log files, this will speed up future executions
print('Checking if Separate log files are created...\n')
if not exists('1 Oct 1994.log'):
    print('Creating Separated Log Files in same Directory as Log Copy...')
    fh = open('1 Oct 1994.log', 'w')
    for li in log1:
        fh.write(f"{li}")
if not exists('2 Nov 1994.log'):
    fh = open('2 Nov 1994.log', 'w')
    for li in log2:
        fh.write(f"{li}")
if not exists('3 Dec 1994.log'):
    fh = open('3 Dec 1994.log','w')
    for li in log3:
        fh.write(f"{li}")
if not exists('4 Jan 1995.log'):
    fh = open('4 Jan 1995.log','w')
    for li in log4:
        fh.write(f"{li}")
if not exists('5 Feb 1995.log'):
    fh = open('5 Feb 1995.log','w')
    for li in log5:
        fh.write(f"{li}")
if not exists('6 Mar 1995.log'):
    fh = open('6 Mar 1995.log','w')
    for li in log6:
        fh.write(f"{li}")
if not exists('7 Apr 1995.log'):
    fh = open('7 Apr 1995.log','w')
    for li in log7:
        fh.write(f"{li}")
if not exists('8 May 1995.log'):
    fh = open('8 May 1995.log','w')
    for li in log8:
        fh.write(f"{li}")
if not exists('9 Jun 1995.log'):
    fh = open('9 Jun 1995.log','w')
    for li in log9:
        fh.write(f"{li}")
if not exists('10 Jul 1995.log'):
    fh = open('10 Jul 1995.log','w')
    for li in log10:
        fh.write(f"{li}")
if not exists('11 Aug 1995.log'):
    fh = open('11 Aug 1995.log','w')
    for li in log11:
        fh.write(f"{li}")
if not exists('12 Sep 1995.log'):
    fh = open('12 Sep 1995.log','w')
    for li in log12:
        fh.write(f"{li}")
if not exists('13 Oct 1995.log'):
    fh = open('13 Oct 1995.log','w')
    for li in log13:
        fh.write(f"{li}")


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



