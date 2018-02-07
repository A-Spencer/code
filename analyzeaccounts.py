
'''
analyzeaccounts.py
Alec Spencer
aspencer18@my.bcit.ca
February 7, 2018
'''

''' Activity Create a /etc/passwd and /etc/groups Analyzer

Create a program that generates a report and saves it to a file.

This report will include a list of all user accounts on your system (UID greater than or equal to 1000) and will include the following data

    Account Name
    UID
    GID
    Home Dir
    Shell
    Supplimentary Groups
'''
def GetGroups(username):
    ''' checks each line of /etc/group file for a match on the parameter "username".
        if found, appends it to a string
        once all lines have been checked, the string is returned
    '''
    # open /etc/group for reading
    with open('/etc/group', 'rt') as groups:   
        while True:
            groupstring = ""
            
            # read in a line from /etc/group
            line = groups.readline()
            
            # break if end of file
            if not line:
                break

            # split line into elements
            line = line.split(":")

            # line[0] = group name
            # line[1] = "x"
            # line[2] = GID
            # line[3:] = username(s)

            # try to match user ("entry") in /etc/group
            # to user ("username", "pwbuffer[0]") stripped from /etc/passwd
            #
            # the first 3 elements in each line are not usernames, so we can skip testing them for a match
            for entry in line[3:]:
                
                # strip the whitespace off of entry, so it can match with username
                entry = entry.strip()

                # if usernames match, append groupstring with matched group
                if (entry == username):
                    groupstring = groupstring + line[0]
                    print(line[0], end=" ")
    groups.close()
    return groupstring



# open files and load lines into buffer, one at a time
with open ('/home/aspencer/analyzeaccounts.log', 'w') as output:
    with open('/etc/passwd', 'rt') as password:

        while True:
            # read in one line
            pwbuffer = password.readline()
            
            # break when end of file reached
            if not pwbuffer:
                break

            # split line into elements
            pwbuffer = pwbuffer.split(":")
            
            # pwbuffer[0] = Account Name
            # pwbuffer[1] = "x"
            # pwbuffer[2] = UID
            # pwbuffer[3] = GID
            # pwbuffer[4] = Full Name
            # pwbuffer[5] = Home Directory
            # pwbuffer[6] = Shell       
            
            # only process accounts with UID >= 1000
            if int(pwbuffer[2]) >= 1000:

                # strip trailing whitespace and newlines from last list item
                pwbuffer[6] = pwbuffer[6].strip()

                print("Account Name: " + pwbuffer[0])
                print("UID: " + pwbuffer[2])
                print("GID: " + pwbuffer[3])
                print("Home Dir: " + pwbuffer[5])
                print("Shell: " + pwbuffer[6])
                print("Supplimentary Groups: ", end="")
                output.write("Account Name: " + pwbuffer[0])
                output.write("\nUID: " + pwbuffer[2])              
                output.write("\nGID: " + pwbuffer[3]) 
                output.write("\nHome Dir: " + pwbuffer[5])
                output.write("\nShell: " + pwbuffer[6])
                output.write("\nSupplimentary Groups: ")
                output.write(GetGroups(pwbuffer[0]) + "\n\n")
                print("\n")
                
        password.close()
    output.close()
