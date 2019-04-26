#!/usr/bin/env python3

###################################
#Run it with the following: 
#python3 print_output.py -c ip_addresses.csv > ./print_output.txt
#
#You will need a CSV file with the following structure:
#device_ip
#10.10.1.1
#10.10.1.2
#10.10.1.3
#
#And finally the script you need (print_output.py):
#########################################

import getpass
import re
import csv

from argparse import ArgumentParser
#from netmiko import ConnectHandler

if __name__ == "__main__":
    parser = ArgumentParser(description='Arguments for running oneLiner.py')
    parser.add_argument('-c', '--csv', required=True, action='store', help='Location of CSV file')
    args = parser.parse_args()
    ssh_username = input("SSH username: ")
    ssh_password = getpass.getpass('SSH Password: ')
with open(args.csv, "r") as file:
        reader = csv.DictReader(file)
        for device_row in reader:
            ssh_session = ConnectHandler(device_type='cisco_ios', ip=device_row['device_ip'],
                                         username=ssh_username, password=ssh_password)
            print("-------- {0} ---------".format(device_row['device_ip']))
            print(ssh_session.send_command("sh inv"))
            print(ssh_session.send_command("sh ip int br"))
