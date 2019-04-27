#!/usr/bin/env python3

##########################################
# Requires package: python3-netmiko
##########################################
#Run it with the following: 
#python3 name_of_program.py -c ip_addresses.csv
#
#You will need a CSV file with the following structure (must include "device_ip"):
#device_ip
#10.10.1.1
#10.10.1.2
#10.10.1.3
#
#########################################



import getpass
import re
import csv

from argparse import ArgumentParser
from netmiko import ConnectHandler

fileout=open("show_cmds_out.txt","w+")

### Main Body ###
if __name__ == "__main__":
    parser = ArgumentParser(description='Arguments for running oneLiner.py')
    parser.add_argument('-c', '--csv', required=True, action='store', help='Location of CSV file')
    args = parser.parse_args()

### User Input usersname/password ###
    ssh_username = input("SSH username: ")
    ssh_password = getpass.getpass('SSH Password: ')

### Begin Main loop ###
with open(args.csv, "r") as file:
        reader = csv.DictReader(file)
        for device_row in reader:
            ### SSH to Device ###
            ssh_session = ConnectHandler(device_type='cisco_ios', ip=device_row['device_ip'],
                                         username=ssh_username, password=ssh_password)
            print("-------- {0} ---------".format(device_row['device_ip']))
            ### Commands to Run on Device ###
            #print(ssh_session.send_command("sh inv"))
            #print(ssh_session.send_command("sh ip int br"))
            #fileout.write("Network Element: ".format(device_row['device_ip']))
            print("Connecting to " + device_row['device_ip'])
            fileout.write("Network Device: " + device_row['device_ip'] + "\n\r")

            ### Commands to Run on Device ###
            #print(ssh_session.send_command("sh inv"))
            fileout.write(ssh_session.send_command("sh ip int br"))
        fileout.close()
