import subprocess
import platform
#from accounts.models import ip_address

def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower() == "windows" else 'c', current_ip_address ), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
                return False

if __name__ == '__main__':
    """
    current_ip_address = ip_address.objects.all()
    print(current_ip_address)
    """
    #current_ip_address = ip_address()
    #current_ip_address.ipaddress()
    current_ip_address = ['127.0.0.1', '10.64.25.35', '10.0.2.15', '192.168.56.101']
    for each in current_ip_address:
        if ping_ip(each):
            print(f"{each} is available")
        else:
            print(f"{each} is not available")



"""
import pyping

r = pyping.ping('google.com')

if r.ret_code == 0:
    print("Success")
else:
    print("Failed with {}".format(r.ret_code))

******


import os
hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'is up!'
else:
  print hostname, 'is down!'


***

import platform   # For getting the operating system name
import subprocess  # For executing a Shell command

def ping(Host):

    Returns True if Host (str) responds to a ping request.
    Remember that a Host may not respond to a ping (ICMP) request even if the Host name is valid.


    # Ping command count option as function of OS
    param = '-n' if platform.system()=='Windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', Host]

    return system.call(command) == 0



!/usr/bin/env python
Django's command-line utility for administrative tasks.
import os
import sys
import pyping

response = pyping.ping('Your IP')

if response.ret_code == 0:
    print("reachable")
else:
    print("unreachable")
"""
