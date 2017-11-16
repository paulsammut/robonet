#!/usr/bin/python

import sys
import argparse
from tempfile import mkstemp
from os import fdopen, remove

robot_name = "primo"
laptop_name = "dev-laptop"

robot_ip = {
        "shop" : "192.168.1.104",
        "VPN"  : "10.8.0.1",
        "field": "192.1.168.0.100"
        }

laptop_ip ={
        "shop" : "192.168.1.142",
        "VPN"  : "10.8.0.2",
        "field": "192.1.168.0.101"
        }

parser = argparse.ArgumentParser(description='Configure the network settings for our robot')
parser.add_argument("-H","--host", help="the host device we are changing settings in",
                                choices=(laptop_name, robot_name))

parser.add_argument("-l","--laptop", help="network the laptop is on",
                                choices=('VPN', 'shop', 'field'))

parser.add_argument("-r","--robot", help="network the robot is on",
                                choices=('VPN', 'shop', 'field'))
args = parser.parse_args()

# Default handler 
if args.host == None:
    args.host = laptop_name

# Handle the dev-laptop host
# Here we open the hosts file and change the primo IP to the appropriate one.
if args.host == laptop_name:
    # create a temp file
    fh, abs_path = mkstemp()
    temp_file = fdopen(fh,'w')

    # read the hosts file
    hosts_file = open("hosts","r").read()

    # print hosts_file

    for line in hosts_file.split("\n"):
        # Find the primo ip entry
        if (robot_name in line) and not "#" in line:
            # Replace the entry with one we want to set
            temp_file.write(
        else:
            temp_file.write(line+"\n")

    print abs_path


