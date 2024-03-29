
'''
user_report_refactored.py
Alec Spencer
aspencer18@my.bcit.ca
February 26, 2018
v1.0
'''

def split_group_line(line):
    '''
    Parameters: line - a single line from /etc/group file
    Returns: a list of group data for an individual group
    '''
    line = line.split(":")
    return line


def parse_groups(file_path='/etc/group'):
    '''
    Parameters: file path (string) with a default of (`/etc/group)
    Returns: nested list of field seperated group data
    Use list comprehension with split_group_line to spit out a nicely formatted list with all supplemental users
    '''
    grouplist = []
    
    # open /etc/group for reading
    with open(file_path, 'rt') as groups:   

        lines = groups.readlines()
        #list comprehension that takes each line of /etc/groups,
        #splits them, then adds them as a list to grouplist list.
        grouplist = [split_group_line(line) for line in lines]
                                
    groups.close()
    return grouplist

def is_user_account(user_data):
    '''
    Parameters: user_data - list comprised of user data from single line of /etc/passwd
    Returns: True if is a user account (includng root) otherwise false
    Moves check out of loop.  Make function that passes in userID, spits out yes/no
    '''
    #pwbuffer = split_group_line(user_data)
    
    if int(user_data[2]) >= 1000:
        return True
    else:
        return False

def get_user_accounts(passwd_file='/etc/passwd'):
    '''
    Parameter: file path (string) with a default of (`/etc/passwd)
    Returns: nested list of user account data (i.e. on element per user account that stores a list of all user account fields)
    Use filter based on above is_user_account
    '''
    user_account_list = []
    listoflists = []
    with open(passwd_file, 'rt') as pwfile:
        
        #parse file into a list of lists
        while True:
            # read in one line
            pwbuffer = pwfile.readline()
            
            # break when end of file reached
            if not pwbuffer:
                break

            # put each line into a list
            listoflists.append(split_group_line(pwbuffer))   
        
        user_account_list = list(filter(is_user_account, listoflists))
        return user_account_list
    
    pwfile.close

def get_sup_groups(user_data, groups):
    '''
    Parameters:
        user_data - single line of /etc/passwd as field seperated list
        groups - nested list of field seperated group data
    Returns: List of the supplimental groups that a user is part of
    '''
    sup_groups_list = []
    sup_groups_list.append([line[0] for line in groups if (line[3].find(user_data[0])!=-1) ])

    return sup_groups_list

def gen_user_report(user_account_list, output_file='user_report.txt'):
    '''
    Parameters:
        user account list
        output file name with default
    Returns: nothing
    This saves the user account list as text file in the specified format to the passed file name.
    This should be done with a for loop
    '''
    with open (output_file, 'w') as output:
    
        for user in user_account_list:        
            output.write("\n\nAccount Name: " + user[0])
            output.write("\nUID: " + user[2])              
            output.write("\nGID: " + user[3]) 
            output.write("\nHome Dir: " + user[5])
            output.write("\nShell: " + user[6])
        
            #prints user's groups
            output.write("Supplimentary Groups: " + str(get_sup_groups(user, parse_groups() )[0] ) )

    output.close()
    
def main():
    '''
    this calls the other functions when script is run as directly, producing the desired report
    '''
    gen_user_report(get_user_accounts())
 
if __name__ == "__main__":
    # execute only if run as a script
    main()