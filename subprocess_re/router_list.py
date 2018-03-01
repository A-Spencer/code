
"""
Router List
~/nasp_python/code/subprocess_re/router_list.py
Alec Spencer
aspencer18@my.bcit.ca
February 28, 2018
v1.0
"""

import subprocess
import re
import pprint

def get_routers(webaddress: str) -> list:
    """
    takes a destination URL string as input, runs traceroute on it, and returns the IP address of each hop in the route

    Args:
        webaddress (str): this can be any publically available IP address or domain name

    Returns:
        routers (str): a list of the IP addresses of each hop in the route

    Example*:
        >>> get_routers('127.0.0.1')
        ['1  127.0.0.1']

    *It is more-or-less impossible to provide a good example for this, since every LAN will return a different result
    """ 
    
    #runs "traceroute -n <URL>"
    tracerouteproc = subprocess.run(
        ["traceroute", "-n", webaddress],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )

    #regex to look for '##  ###.###.###.###', give or take a few digits
    ipv4_regex = r"\d+  \d+\.\d+\.\d+\.\d+"

    #finds all instances of the pattern 'ipv4_regex' in the string 'tracerouteproc.stdout'
    #and puts them in the variable 'routers' as a list of strings
    routers = re.findall(ipv4_regex, tracerouteproc.stdout)

    return routers

def make_dictionary(somedictionary: dict, routerlist: list) -> dict:
    '''
    Assembles (or adds to) a dictionary using a list of router IP addresses and their hop distance from the local host
    
    Args:
        somedictionary (dict): a (potentially empty) dictionary in the form of {"IP Address": "[hopnumber, number of occurances]"}
        routerlist (list): a list of of hop numbers and IP addresses

    Returns:
        a dictionary in the form of {"IP Address": "[hopnumber, number of occurances]"}

    Example:
        >>> mydictionary = {}
        ... make_dictionary(mydictionary, ['1  192.168.1.254', '2  10.31.40.1', '3  154.11.10.9'])
        {'192.168.1.254': ['1', 1], '10.31.40.1': ['2', 1], '154.11.10.9': ['3', 1]}

    '''

    for eachline in routerlist:
        
        #strip the ip address
        ipaddy = re.search(r"\d+\.\d+\.\d+\.\d+", eachline).group()
        
        #strip the hop number
        hopnumber = re.search(r"\d+", eachline).group()

        if ipaddy in somedictionary.keys():
            #if already present in the dictionary,
            #increment the second value (the "number of occurances")
            somedictionary[ipaddy][1] = somedictionary[ipaddy][1] + 1
        
        else:
            #if not in dictionary, add ip address as a new key
            #include its hop number and set number of occurances to 1.
            somedictionary[ipaddy] = [hopnumber, 1]

    return somedictionary

def print_dictionary(somedictionary: dict) -> None:
    '''
    Prints the specific type of dictionary created in the make_dictionary function

    Args:
        somedictionary (dict): a dictionary in the form of {"IP Address": "[hopnumber, number of occurances]"}

    Returns:
        None

    Example:
        >>> mydictionary = {'192.168.1.254': ['1', 1], '10.31.40.1': ['2', 1]}
        ... print_dictionary(mydictionary)
        192.168.1.254
          Hop number: 1
          Number of occurances: 1

        10.31.40.1
          Hop number: 2
          Number of occurances: 1

    '''

    for eachentry in somedictionary:
        print(eachentry)
        print("  Hop number: " + str(somedictionary[eachentry][0]))
        print("  Occurances: " + str(somedictionary[eachentry][1]) + "\n")
    return


def main():
    '''
    prints all the routers between the host and a variety of websites
    '''

    routestotrace = ["8.8.8.8", "www.osnews.com", "www.yahoo.com", "www.facebook.com", "www.google.com"]
    
    #dictionary in the form of {"IP Address": "[hopnumber, number of occurances]"}
    newdictionary = dict()

    #iterate through each route, printing the router ip addresses along the way and then adding them to a dictionary
    for url in routestotrace:
        print("\n" + url)
        pprint.pprint(get_routers(url))
        make_dictionary(newdictionary, get_routers(url))

    print("\n\n********************\n* Bonus Dictionary *\n********************\n")

    print_dictionary(newdictionary)


if __name__ == "__main__":
    # execute only if run as a script
    main()