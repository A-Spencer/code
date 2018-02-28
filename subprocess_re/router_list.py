
"""
router_list.py
Alec Spencer
aspencer18@my.bcit.ca
February 28, 2018
v0.01
"""
"""
You will create a program router_list.py that will print a list of routers used by your workstation to access the following sites:

    8.8.8.8
    www.osnews.com
    www.yahoo.com
    www.facebook.com
    www.google.com

This will be accomplished by creating a function: get_routers that accepts an IP address or DNS as its only parameter and returns a list of routers.

This function will utilize the subprocess module to invoke tracert and capture its output.

This output will use a regular expression to extract all of the IP address of the routers.

A function main will loop over all of the required destinations and create a master list of all routers used to access all of the destinations.

It will then print this list.
Bonus

Create a dictionary of routers that stores both there distance (hop count from host), and frequency of use (i.e. how many times they were used for all of the destinations)
Code Structure

This code will be stored in ~/nasp_python/subprocess_re/
"""

import subprocess
import re
import pprint

def get_routers(webaddress: str) -> list:
    """
    takes a destination URL string as input and returns the ip address of each hop in the route
    """

 ''' 
    tracerouteproc = subprocess.run(
        ["traceroute", "-n", webaddress],
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True
    )
   
    #get rid of that pesky trailing newline
    tracerouteproc.stdout = tracerouteproc.stdout.strip()
    
    #make a list of lines in tracerout
    traceroutelist = []
    for string in tracerouteproc.stdout.split("\n"):
        traceroutelist.append([string])
 '''

    traceroutelist = [['traceroute to www.facebook.com (31.13.76.68), 30 hops max, 60 byte packets'], [' 1  142.232.221.254  1.321 ms  1.346 ms  1.330 ms'], [' 2  142.232.24.123  0.646 ms  0.688 ms  0.680 ms'], [' 3  142.232.38.94  0.443 ms  0.464 ms  0.453 ms'], [' 4  142.232.38.133  0.617 ms * *'], [' 5  192.68.70.22  0.978 ms  0.871 ms  0.859 ms'], [' 6  134.87.0.74  1.898 ms  1.802 ms  1.962 ms'],[' 7  199.212.24.64  2.075 ms  2.004 ms  2.230 ms'], [' 8  206.81.82.189  5.491 ms  5.438 ms  5.297 ms'], [' 9  206.81.80.211  5.529 ms  5.487 ms  6.426 ms'], ['10  157.240.48.51  5.026 ms 157.240.48.53  4.863 ms 157.240.48.57  5.140 ms'], ['11  173.252.67.121  4.871 ms 173.252.67.25  5.130 ms 173.252.67.35  5.109 ms'], ['12  31.13.76.68  6.227 ms  4.962 ms  5.133 ms']]
    
    print(traceroutelist)

    #regex to look for '##  ###.###.###.###', give or take a few digits
    ipv4_regex = r"\d{1,2}  \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    routers = list

    #for eachline in traceroutelist:
    #    routers = re.match(r"\d{1,2}  \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", '1  142.232.221.254  1.348 ms  1.403 ms  1.388 ms\n2  142.232.24.123  0.963 ms  1.037 ms  1.028 ms\n 3  142.232.38.94  0.447 ms  0.449 ms  0.438 ms\n 4  142.232.38.133  0.614 ms  0.605 ms  0.641 ms\n 5  192.68.70.22  0.935 ms  0.920 ms  0.903 ms\n 6  134.87.0.74  1.963 ms  2.046 ms  2.046 ms\n 7  199.212.24.64  2.265 ms  2.019 ms  2.690 ms\n 8  206.81.82.189  5.568 ms5.502 ms  5.462 ms\n 9  206.81.80.211  5.577 ms  5.557 ms  5.528 ms\n10  157.240.48.53  5.122 ms  5.018 ms 4.883 ms\n11  173.252.67.35  4.869 ms 173.252.67.159  5.125 ms 173.252.67.123  4.913 ms\n12  31.13.76.685.218 ms  5.149 ms  5.210 ms\n", stderr="")')
    #    print(routers)
        #routers = routers.group()
    #m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
    #print(m.group())

    return routers


def main():

    routestotrace = ["8.8.8.8", "www.osnews.com", "www.yahoo.com", "www.facebook.com", "www.google.com"]

    #for url in routestotrace:
    #    get_routers(url)
    get_routers('www.facebook.com')

if __name__ == "__main__":
    # execute only if run as a script
    main()