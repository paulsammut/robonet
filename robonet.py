#!/usr/bin/python

import sys
import argparse
from tempfile import mkstemp
from os import fdopen, remove, chmod
from shutil import move

robot_name = "primo"
laptop_name = "dev-laptop"
hosts_fp = "/etc/hosts"              # hosts file path
zshrc_fp = ".zshrc"

# Create the dictionaries for the ip addresses
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

def configHosts(remote_host_name, remote_host_ip):
    # create a temp file
    fh, abs_path = mkstemp()
    temp_file = fdopen(fh,'w')

    # read the hosts file
    hosts_file = open(hosts_fp,"r").read()

    for line in hosts_file.split("\n"):
        # Find the remote host ip entry
        if (remote_host_name in line) and not "#" in line:
            # Replace the entry with one network and remote host name
            temp_file.write(remote_host_ip + " " + remote_host_name + "\n")
        else:
            temp_file.write(line+"\n")

    # remove the original file
    remove(hosts_fp)

    # move the modified hosts file to replace it
    move(abs_path, hosts_fp)

    # change the permissions
    chmod(hosts_fp, 0644)

    print "Set " + remote_host_name + " with ip " + remote_host_ip 

def configROSMASTER(master_host_name):
    # create a temp file
    fh, abs_path = mkstemp()
    temp_file = fdopen(fh,'w')

    # read the current .zshrc file
    zshrc_file = open(zshrc_fp,"r").read()

    new_uri = "export ROS_MASTER_URI=http://"+master_host_name+":11311\n";

    for line in zshrc_file.split("\n"):
        # Find the ROS_MASTER entry
        if ("export ROS_MASTER_URI" in line) and (not "#" in line):
            # Replace the entry with one network and remote host name
            temp_file.write(new_uri)
        else: 
            temp_file.write(line+"\n")

    # remove the original file
    remove(zshrc_fp)

    # move the modified hosts file to replace it
    move(abs_path, zshrc_fp)

    # change the permissions
    chmod(zshrc_fp, 0644)

    print "Set the ROS_MASTER_URI to: " + new_uri


if __name__ == "__main__":

    # Handle the argument parsing
    parser = argparse.ArgumentParser(description='Configure the network settings for our robot')
    parser.add_argument("-H","--host", help="the host device we are changing settings in",
                                    choices=(laptop_name, robot_name))

    parser.add_argument("-n","--network", help="network the devices are on",
                                    choices=('VPN', 'shop', 'field'))

    args = parser.parse_args()

    # Default host handler 
    if args.host == None:
        args.host = laptop_name

    # Handle the dev-laptop host
    # Here we open the hosts file and change the primo IP to the appropriate one.
    if args.host == laptop_name:
        # Make a check to make sure the network arguments have been added
        if args.network == None:
            print "Network must be specified!"
            quit()
        #
        configHosts(robot_name, robot_ip.get(args.network))

