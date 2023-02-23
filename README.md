# cookies.py
![](image/cookie.png)

Simple script for converting a cookies.json file (exported from the 'Cookies Quick Manager' Firefox browser plugin) to a Netscape standard formatted cookies.txt file suitable for use with httrack. This script takes one argument, which is the relative path to the cookies.json file.

```
Usage: python3 cookies.py ./cookies.json 
```

The above example is for a case where the cookies.json file is located in the same directory as this script. It will output the corresponding cookies.txt file to the script's working directory. 
