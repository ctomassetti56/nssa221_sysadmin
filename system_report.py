#!/usr/bin/python3

# @author Christian Tomassetti
# @nssa221.01
# @script02 assignment
# @project system_report

import os
import subprocess
import sys
import platform
import socket

os.system('clear') # clears the terminal for cleaner look

def device_information():
    print("Device Information:")
    hostname = platform.node()
    domain = socket.getfqdn()
    print("Hostname:\t\t" + str(hostname))
    print("Domain:\t\t\t" + str(domain))

def main():
    device_information()

if __name__ == '__main__':
    main()