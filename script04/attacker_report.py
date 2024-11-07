#!/usr/env/bin python3

# Author: Christian Tomassetti
# NSSA221.01
# Script04 Assignment
# Project: Attacker Report

#INSTALLATIONS REQUIRED:
#NOTE The script will attempt to install the libraries if they cannot be found.
#NOTE If you are not sure if you have the libraries installed, you may run the script to check.
#NOTE OR manually install the libraries using the following commands:

#NOTE For virutal environment:
# python3 -m pip install python-geoip-python3
# python3 -m pip install python-geoip-geolite2

#NOTE For global environment:
# pip3 install python-geoip-python3
# pip3 install python-geoip-geolite2

import datetime
import os
import re

#GLOBAL VARIABLES:
#Key terms for intrusion detection:
trigger_words = ['Failed password for root from', 
                 'pam_succeed_if(sshd:auth): requirement \"uid >= 1000\" not met by user',
                 'PAM 5 more authentication failures;',
                 'pam_unix(sshd:auth): authentication failure;',
                 ]

#amount of failed attempts per IP address before being flagged:
failed_attempts_allowed = 10

#dictionary to associate IP addresses with their failed attempts:
failed_attempts = {}

# Report shows ten or more failed attempts.
# Report shows headers, count, IP address, and country.
# Report shows current date.
# Count is sorted in ascending order.
# Regex is used to find the IP address.
# Report identifies IP address and country of origin.

# Check for required libraries
try:
    from geoip import geolite2
except ImportError:
    print("Error: Missing required library 'geoip'.")
    print("attempitng to install now...")
    if os.environ.get('VIRTUAL_ENV'):
        os.system('python3 -m pip install python-geoip-python3')
        os.system('python3 -m pip install python-geoip-geolite2')
    else:
        os.system('pip3 install python-geoip-python3')
        os.system('pip3 install python-geoip-geolite2')
    try:
        from geoip import geolite2
    except ImportError:
        print("Error: 'geoip' failed to install. Please try again.")
    else:
        print("Success: 'geoip' has been installed.")
        from geoip import geolite2

def report_stamp():
    fullDate = datetime.datetime.now()
    formatDate = fullDate.strftime("%B %d, %Y")
    print("\033[92mAttacker Report\033[0m - " + formatDate)

def read_log():
    # use regex to find IP address
    with open('script04/syslog.log') as dataFile:
        for line in dataFile:
            for phrase in trigger_words:
                if phrase in line:
                    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
                    if ip in failed_attempts.keys():
                        failed_attempts[ip] += 1
                    else:
                        failed_attempts[ip] = 1


def main():
    os.system('clear')
    report_stamp()
    print()
    read_log()
    for key in failed_attempts.keys:
        print(key)
    # for ipaddress in failed_attempts.keys():
    #     print(str(ipaddress))
        # print(str(ipaddress) + "    Count: " + str(failed_attempts[ipaddress]))
            # match = geolite2.lookup(ipaddress)
            # print("\033[91m" + str(failed_attempts[ipaddress]) + "\033[0m failed attempts from \033[91m" + ipaddress + "\033[0m located in \033[91m" + match.country + "\033[0m")

if __name__ == "__main__":
    main()
