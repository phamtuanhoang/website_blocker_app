import time
from datetime import datetime as dt

hosts_path = "/etc/hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]


#start for while loop
while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
        with open(hosts_path,'r+') as file:
            content=file.read()
            print content
            #iterate in array
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
        print "Working hours"
    else:
        print "sleep hour"

    time.sleep(5)
