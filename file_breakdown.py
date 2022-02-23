# Seperate log file into separate files by month
f = open('log_file.txt', 'w')

for line in f: 
    if "/Jan/" in line:
       Jan_log = open("Jan_log.txt", 'w')
       Jan_log.write(line)
    
    elif "/Feb/" in line:
        Feb_log = open("Feb_log.txt", 'w')
        Feb_log.write(line)

    elif "/Mar/" in line:
        Mar_log = open("Mar_log.txt", 'w')
        Mar_log.write(line)

    elif "/Apr/" in line:
        Apr_log = open("Apr_log.txt", 'w')
        Apr_log.write(line)

    elif "/May/" in line:
        May_log = open("May_log.txt", 'w')
        May_log.write(line)

    elif "/Jun/" in line:
        Jun_log = open("Jun_log.txt", 'w')
        Jun_log.write(line)

    elif "/Jul/" in line:
        Jul_log = open("Jul_log.txt", 'w')
        Jul_log.write(line)

    elif "/Aug/" in line:
        Aug_log = open("Aug_log.txt", 'w')
        Aug_log.write(line)

    elif "/Sep/" in line:
        Sep_log = open("Sep_log.txt", 'w')
        Sep_log.write(line)

    elif "/Oct/" in line:
        Oct_log = open("Oct_log.txt", 'w')
        Oct_log.write(line)

    elif "/Nov/" in line:
        Nov_log = open("Nov_log.txt", 'w')
        Nov_log.write(line)

    elif "/Dec/" in line:
        Dec_log = open("Dec_log.txt", 'w')
        Dec_log.write(line)
