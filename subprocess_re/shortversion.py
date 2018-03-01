import subprocess
import re
def get_routers(webaddress: str) -> list:    
    tracerouteproc = subprocess.run(["traceroute", "-n", webaddress], stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    routers = re.findall(r"\d+  \d+\.\d+\.\d+\.\d+", tracerouteproc.stdout)
    return routers
routestotrace = ["8.8.8.8", "www.osnews.com", "www.yahoo.com", "www.facebook.com", "www.google.com"]
for url in routestotrace:
	print("\n" + url + "\n" + str(get_routers(url)))