# roboset

roboset is a utility that sets up the computer's networking settings to work with
primo either at home or at the shop. I wrote this after getting tired of editing the
hosts file manually on two computers and opening a vpn every morning.

# What roboset does

* Take in a host argument (-h):
    * laptop (default)
    * primo
* Take in a location argument (-l):
    * home (default)
    * shop
* Modify /etc/hosts file and put in the right ip
* If home, also open a vpn connection to primo
* SSH into primo and run a script a command that sets the correct dev-laptop IP in
  the hosts fil
