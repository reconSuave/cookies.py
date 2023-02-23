"""
Simple script for converting a cookies.json file exported 
from the 'Cookies Quick Manager' Firefox browser plugin 
to a Netscape standard formatted cookies.txt file suitable
for use with httrack. This script takes one argument, which 
is the relative path to the cookies.json file.

Usage: python3 cookies.py ./cookies.json 

The above example is for a case where the cookies.json file 
is located in the same directory as this script. It will 
output the corresponding cookies.txt file to the script's 
working directory. 
"""

import datetime
import json
import os 
import sys
cookie = os.path.join(cwd, sys.argv[1]) # sys.argv[1] is relative path to cookies.json

with open(cookie, 'r') as f:
    x = f.read()
    data = json.loads(x) 
    with open('cookies.txt', 'w') as g:
        for x in range(0, len(data)):
            host_full = data[x]["Host raw"]
            host = host_full.split('//')[1].split('/')[0] #first split drops "https://" and second split drops tailing '/'
            path = data[x]["Path raw"]
            content = data[x]["Content raw"]
            expires = data[x]["Expires raw"]
            name = data[x]["Name raw"]
            if data[x]["HTTP only raw"] == "false":
                secure = "TRUE"
            else:
                secure = "FALSE"
            g.write(host + "\t" + "TRUE\t" +  path + "\t" + secure + "\t" + expires + "\t" + name + "\t" + content + "\n")
