
'''
user_report.py
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
def parse_groups(file_path='/etc/group'):
    ''' checks each line of /etc/group file for a match on the parameter "username".
        if found, appends it to a string
        once all lines have been checked, the string is returned
    '''
    grouplines = []

    # open /etc/group for reading
    with open(file_path, 'rt') as groups:   

        while True:
            # read in a line from /etc/group
            line = groups.readline()
            line = line.strip()

            # break if end of file
            if not line:
                break

            # put each line into a list
            grouplines.append([line])
                        
    groups.close()
    return grouplines

def parse_accounts(file_path='/etc/passwd'): 
    
    userlist = []
    
    # open files and load lines into buffer, one at a time
    with open(file_path, 'rt') as password:

        while True:
            # read in one line
            pwbuffer = password.readline()
            
            # break when end of file reached
            if not pwbuffer:
                break

            # put each line into a list
            userlist.append([pwbuffer])       
                  
    password.close()
    return userlist


def gen_user_report(user_account_list, output_file='./user_report.txt'): 

    with open (output_file, 'w') as output:
    
        for index in range(len(user_account_list)):
            
            # make a buffer to process each line
            pwbuffer = str(user_account_list[index])
            
            # strip square brackets, quotes, and /n
            pwbuffer = pwbuffer[2:len(pwbuffer)-4]

            # split into separate elements:
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
                output.write("Account Name: " + pwbuffer[0])
                output.write("\nUID: " + pwbuffer[2])              
                output.write("\nGID: " + pwbuffer[3]) 
                output.write("\nHome Dir: " + pwbuffer[5])
                output.write("\nShell: " + pwbuffer[6])
                output.write("\nSupplimentary Groups: ")
                


                for line in parse_groups():
                        
                    # change all colons to commas (just to make all delimiters the same)
                    line = line[0].replace(":", ",")
                    
                    # split into separate elements
                    line = line.split(",")
                    # line[0] = group name
                    # line[1] = "x"
                    # line[2] = GID
                    # line[3:] = username(s)

                    # try to match user stripped from /etc/group
                    # to user stripped from /etc/passwd
                    #
                    # ignore the first 3 elements in each line are not usernames, so we can skip testing them for a match
                    for entry in line[3:]:
                        
                        # strip the whitespace off of entry, so it can match with username
                        entry = entry.strip()

                        # if usernames match, append groupstring with matched group
                        if (entry == pwbuffer[0]):
                            output.write(line[0] + " ")

                output.write("\n\n")
                            
        output.close()

def main():
    gen_user_report(parse_accounts())

if __name__ == "__main__":
    # execute only if run as a script
    main()