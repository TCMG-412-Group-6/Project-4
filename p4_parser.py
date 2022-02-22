from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY
import os
from datetime import datetime
import urllib.request
import re


# Downlad log file if it does not exist already
FilePath = './log_file.txt'
FileExists = os.path.exists(FilePath)

if FileExists == False:
    print("Downloading the file")
    url = "https://s3.amazonaws.com/tcmg476/http_access_log"
    urllib.request.urlretrieve(url,"./log_file.txt")

else:
    print ("File already exists")

# Opens file
log_file = open("log_file.txt", 'r')

#conter for requests
total_count = 0

months = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0
}

days = {
    MONDAY: 0,
    TUESDAY: 0,
    WEDNESDAY: 0,
    THURSDAY: 0,
    FRIDAY: 0,
    SATURDAY: 0,
    SUNDAY: 0

}

# Start parsing by separating sections into a list
regex = re.compile("(.*?) - - \[(.*?):(.*) .*\] \"[A-Z]{3,6} (.*?) HTTP.*\" (\d{3}) (.+)")

for line in log_file:
    total_count = total_count = total_count + 1

    sections = regex.split(log_file)

    if len(sections) != 8:
        continue

    datestamp = datetime.strptime(sections[2], '%d/%b/%Y')

    months[datestamp.month] += 1
    print(datestamp.month)
# I do not know if I should use isoweekday or just weekday
    days[datestamp.weekday] += 1
    print(datestamp.weekday)
    
    
print(months)
print(days)

log_file.close()




















