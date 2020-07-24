#open file
fh = open('mbox-short.txt','r')

#count iteration variable
count = 0
#star to scan the file
for line in fh:
    #Split lines into a emallist
    emaillist = line.split()
    #Picked up all lines start with "From"
    if line.startswith('From'):
    #Exclude all lines saarting with "From:" (Note, the differentces)
        if line.startswith('From:'):
            continue
    #For the rest lines that starting with "From" not "From:", count how many lines are like this
        else:
            count = count + 1
            print(emaillist[1])
    #Print the second position [1] part which should be the email address

print("There were", count, "lines in the file with From as the first word")
