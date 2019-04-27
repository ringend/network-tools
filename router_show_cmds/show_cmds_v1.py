#!/usr/bin/env python3

##########################################
# Requires package: python3-netmiko
##########################################
#Run it with the following: 
#python3 name_of_program.py -c device_name_or_ip.csv
#
#You will need a CSV file with the following structure (must include "device_ip"):
#device_ip
#10.10.1.1
#10.10.1.2
#10.10.1.3
#
###########################################
# Remember to set the section the username/password section below
###########################################

import getpass
import re
import csv

from argparse import ArgumentParser
from netmiko import ConnectHandler
from datetime import date
from datetime import time
from datetime import datetime

### Main Body ###
if __name__ == "__main__":
    parser = ArgumentParser(description='Arguments for running oneLiner.py')
    parser.add_argument('-c', '--csv', required=True, action='store', help='Location of CSV file')
    args = parser.parse_args()

    ############## USERNAME/PASSWORD SECTION ######################
    ##### Uncommmit next two line for user input of username/password ###
    #ssh_username = input("SSH username: ")
    #ssh_password = getpass.getpass('SSH Password: ')
    ##### Uncommit next two lines for hardcoded username/password ###
    ssh_username = "cisco"
    ssh_password = "cisco"
    ###############################################################

    ### Create Output File ###
    fileout=open("show_cmds_out.txt","w+")

### Begin Main loop ###
with open(args.csv, "r") as file:
        reader = csv.DictReader(file)
        for device_row in reader:
            ### SSH to Device ###
            ssh_session = ConnectHandler(device_type='cisco_ios', ip=device_row['device_ip'],
                                         username=ssh_username, password=ssh_password)

            ### Write to Screen and File ###
            print("Connecting to " + device_row['device_ip'] + " @ " + format(datetime.today()) + " ...")
            fileout.write("===Network Device: " + device_row['device_ip'] + " @ "+ format(datetime.today()) + "\n\r")

            ### Commands to Run on Device ###
            #fileout.write(ssh_session.send_command("sh inv"))
            fileout.write(ssh_session.send_command("sh ip int br"))
            fileout.write("\n\r")

        print("Finished")
        fileout.close()
