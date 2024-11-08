#!/usr/bin/env python3

# Author: Christian Tomassetti
# NSSA221.01
# Script04 Assignment
# Project: Attacker Report

# INSTALLATIONS REQUIRED:
# NOTE The script will attempt to install the libraries if they cannot be found.
# NOTE If you are not sure if you have the libraries installed, you may run the script to check.
# NOTE OR manually install the libraries using the following commands:

# NOTE For virtual environment:
# python3 -m pip install python-geoip-python3
# python3 -m pip install python-geoip-geolite2

# NOTE For global environment:
# pip3 install python-geoip-python3
# pip3 install python-geoip-geolite2

import datetime
import os
import re

# GLOBAL VARIABLES:
# Key terms for intrusion detection:
trigger_words = [
    'Failed password for root from',
    'pam_succeed_if(sshd:auth): requirement "uid >= 1000" not met by user',
    'PAM 5 more authentication failures;',
    'pam_unix(sshd:auth): authentication failure;',
]

# Amount of failed attempts per IP address before being flagged:
failed_attempts_allowed = 10

# Dictionary to associate IP addresses with their failed attempts:
failed_attempts = {}

# Check for required libraries
try:
    from geoip import geolite2
except ImportError:
    print("Error: Missing required library 'geoip'.")
    print("Attempting to install now...")
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
    # Use regex to find IP address
    with open('/home/student/Sysadmin/nssa221_sysadmin/script04/syslog.log') as dataFile:
        for line in dataFile:
            for phrase in trigger_words:
                if phrase in line:
                    ip_match = re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', line)
                    if ip_match:
                        ip = ip_match.group()
                        if ip in failed_attempts:
                            failed_attempts[ip] += 1
                        else:
                            failed_attempts[ip] = 1

def main():
    os.system('clear')
    report_stamp()
    print()
    read_log()
    #sort the dictionary by value
    sorted_attempts = dict(sorted(failed_attempts.items(), key=lambda item: item[1], reverse=False))
    print("  IP Address\t\t  Failed Attempts\t\tCountry")
    print("---------------------------------------------------------")
    for ip, count in sorted_attempts.items():
        if count >= failed_attempts_allowed:
            match = geolite2.lookup(ip)
            country = match.country if match else "Unknown"
            print(f"{ip}\t\t\t{count}\t\t\t  {country}")

if __name__ == "__main__":
    main()