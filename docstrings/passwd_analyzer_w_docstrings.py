#! /usr/bin/env
'''
passwd_analyzer_w_docstrings.py
Alec Spencer
aspencer18@my.bcit.ca
February 26, 2018
v1.0
'''

def split_group_line(line: str) -> list:
    '''
    Splits a string into a list individual strings

    Args:
        line (str): a single line from /etc/group file
    
    Returns:
        line (list): a list of group data for an individual group
    
    Example:

        >>> split_group_line('root:x:0:0:root:/root:/bin/bash\\n')
        ['root', 'x', '0', '0', 'root', '/root', '/bin/bash\\n']
    '''

    line = line.split(":")
    return line


def parse_groups(file_path='/etc/group') -> list:
    '''
    Opens a file in the format of /etc/group and makes a nested list where each line is a list entry,
    and each line is further split into a list of individual strings.

    Args:
        file_path (str): a file name from which to read group data, with a default of /etc/group

    Returns:
        grouplist (list): a nested list of field seperated group data containing all supplemental users

    Example:
        >>> parse_groups('./group.truncated')
        [['wheel', 'x', '10', 'bigmoocow,littlemoocow\\n'], ['tcpdump', 'x', '72', '\\n'], ['bigmoocow', 'x', '1000', 'bigmoocow\\n']]
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

def is_user_account(user_data: list) -> bool:
    '''
    Takes a list as input and checks if the third element is a valid linux UID, returning true or false.

    Args:
        user_data (list): a list comprised of user data from single line of /etc/passwd
    
    Returns:
        True (bool): returns if user_data is a user account 
        False (bool): returns if user_data is not a user account

    Example:
        >>> is_user_account(['root', 'x', '0', '0', 'root', '/bin/bash\\n'])
        False    
    '''
    
    if int(user_data[2]) >= 1000:
        return True
    else:
        return False

def get_user_accounts(passwd_file='/etc/passwd') -> list:
    '''
    Args:
        passwd_file (str): a file path (string) with a default of /etc/passwd

    Returns: 
        user_account_list (list): a nested list of user account data (i.e. one element per user account that stores a list of all user account fields)
    
    Example:
        >>> get_user_accounts('./passwd.truncated')
        [['bigmoocow', 'x', '1000', '1000', 'Big Moo Cow', '/home/bigmoocow', '/bin/bash\\n'], ['littlemoocow', 'x', '1001', '1001', 'Little Moo Cow', '/home/littlemoocow', '/bin/bash\\n']]
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

def get_sup_groups(user_data: list, groups: list) -> list:
    '''
    Matches a username from /etc/passwd to usernames in /etc/group to determine which groups a user belongs to

    Parameters:
        user_data (list): single line of /etc/passwd as field seperated list
        groups (list): nested list of field separated group data

    Returns:
        sup_groups_list (list): a list of the supplemental groups that a user is part of
    
    Example:
        >>> get_sup_groups('bigmoocow:x:1000:1000:Big Moo Cow:/home/bigmoocow:/bin/bash', parse_groups('./group.truncated'))
        [['wheel', 'bigmoocow']]
    '''
    
    sup_groups_list = []
    sup_groups_list.append([line[0] for line in groups if (line[3].find(user_data[0])!=-1) ])
    return sup_groups_list

def gen_user_report(user_account_list: list, output_file='user_report.txt') -> None:
    '''
    This saves the user account list as text file in the specified format to the passed file name.
    This should be done with a for loop
    
    Args:
        user_account_list (list): a list of lines from 
        output_file (str): output file to write to, with default as 'user_report.txt'

    Returns:
        None
    '''
    with open (output_file, 'w') as output:
    
        for user in user_account_list:        
            output.write("Account Name: " + user[0])
            output.write("\nUID: " + user[2])              
            output.write("\nGID: " + user[3]) 
            output.write("\nHome Dir: " + user[5])
            output.write("\nShell: " + user[6])
        
            #prints user's groups
            output.write("Supplimentary Groups: " + str(get_sup_groups(user, parse_groups() )[0] ) )
            output.write("\n\n")

    output.close()
    
def main():
    '''
    this calls the other functions when script is run directly, producing the desired report
    '''
    gen_user_report(get_user_accounts())
   
if __name__ == "__main__":
    main()