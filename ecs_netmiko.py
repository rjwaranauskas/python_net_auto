# -----------------------------------------------
# ------Basic Netmiko Cisco iOS Manipulation-----
# Automates the speed and duplex of 1 interface--
# ----and writes changes to two output files-----
# -----Written by Richard Waranauskas 8/3/18-----
# -----------------------------------------------
#NOTE: In its current state, this does NOT save anything from run to start!

from netmiko import Netmiko #or could be import ConnectHandler
from getpass import getpass
import os, sys, re
from pprint import pprint

my_device= {
    'ip':"8.8.8.8", #if using ssh instead of telnet, "ip" should be "host" (i.e. test.com)
    'username':'username', #not needed in telnet - used in ssh
    'password': getpass(),
    'secret' : 'cisco',
    'device_type':'cisco_ios_telnet'
}

net_conn = Netmiko(**my_device)

#Set a list of commands to send to the device.
cfg_commands = ["int fa1/0/8", "speed 100", "duplex half"] #this list is for commands that are instant (int, speed, etc) - use global_delay_factor or \n to do multi-line commands (i.e. del)
net_conn.enable()
output = net_conn.send_config_set(cfg_commands)
#print(output) #may not be needed since config_set displays the output already.


# -----------------------------------------------
# ------Printing operations (write to file)------
# -----------------------------------------------

filename = "changes.txt"
with open(filename, mode='w') as f:
	f.write(output)
	print(f"Wrote to {filename} at {os.path.dirname(os.path.abspath(filename))}")


testout = net_conn.send_command("show ip int br")
filename = "cisco_output_test2.txt"
with open(filename, mode='w') as f:
	f.write(testout)
	print(f"Wrote to {filename} at {os.path.dirname(os.path.abspath(filename))}")

net_conn.disconnect()
print("Disconnected from device.")