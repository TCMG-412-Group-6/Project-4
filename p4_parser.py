from calendar import FRIDAY, MONDAY, SATURDAY, SUNDAY, THURSDAY, TUESDAY, WEDNESDAY
import os
from datetime import datetime
import urllib.request
import re
from collections import Counter


# Downlad log file if it does not exist already
FilePath = './log_file.txt'
FileExists = os.path.exists(FilePath)

if FileExists == False:
    print("Downloading the file")
    url = "https://s3.amazonaws.com/tcmg476/http_access_log"
    urllib.request.urlretrieve(url,"./log_file.txt")

else:
    print ("File already exists")
#File should already be downloded
# Opens file
log_file = open("log_file.txt", 'r')

#couter for requests
total_count = 0
redirection_codes = 0
client_errors = 0


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
    total_count = total_count + 1

    sections = regex.split(log_file)

    if len(sections) != 8:
        continue

    datestamp = datetime.strptime(sections[2], '%d/%b/%Y')

    months[datestamp.month] += 1
    print(datestamp.month)
# I do not know if I should use isoweekday or just weekday
    days[datestamp.weekday] += 1
    print(datestamp.weekday)

    #Get codes for redirection and client errors
    
    if re.search(sections[6]) == "3**":
        redirection_codes =+ 1
    if re.search(sections[6]) == "4**":
        client_errors =+ 1
# Attempting to find the most/least common file
    counter = Counter(log_file)
    most_requested = counter.most_common(sections[5])
# From what I have read the negative at end is suppose to give the opposite
    least_requested = counter.most_common(sections[5])[-1] 
    



percent_redirected = int(redirection_codes)/int(total_count)*100
percent_client_errors = int(client_errors)/int(total_count)*100
        
print("The total amount of requests: ", total_count)
print("The total requests for each month : /n", months)
print("The total requests for each day of the week: /n", days)
print("The percentage of redirected requests: ", percent_redirected)
print("The percentage of requests that led to client error: ", percent_client_errors)
print("The most request file was: ", most_requested)
print("The most request file was: ", least_requested)

log_file.close()
