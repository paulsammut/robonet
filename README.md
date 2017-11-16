# robonet

roboset is a utility that sets up the computer's networking settings to work with
primo either at home or at the shop. I wrote this after getting tired of editing the
hosts file manually on two computers and opening a vpn every morning.

## What robonet does

* Take in a host argument (-H):
    * dev-laptop 
    * primo
* Take in a network argument (-n):
    * home (default)
    * shop
    * field
* Take a ROS_MASTER argument (-r):
    * primo
    * dev-laptop

* Modify /etc/hosts file and put in the right ip
* If ROS_MASTER argument provided, set it in the ~/.zshrc file.

Script must be run as sudo to edit the /etc/hosts file

