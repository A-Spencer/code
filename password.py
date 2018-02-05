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


with open('/etc/passwd', 'rt') as fin
    fin.readline()