#!/usr/bin/python3

# @author Christian Tomassetti
# @nssa221.01
# @script01 assignment
# @project ping_test

# a script that gives the user 5 menu options including displaying the computers gateway,
# pinging the default gateway address, pinging the RIT DNS address, testing connection to the
# google server, and exiting the program. The program is linux compatable and will not run
# in the windows terminal due to linux specific commands. Most of the code that uses subprocess.run
# was discovered through the Pydocs documentation website or learned in class from lecture or
# code written on the white board.

import os
import subprocess
import sys

os.system('clear') # clears the terminal for cleaner look

def printMenu():
    # prints the menu options that the user can choose from
    print("1.) Display the default gateway \n" +
          "2.) Test Local Connectivity \n" +
          "3.) Test Remote Connectivity \n" +
          "4.) Test DNS Resolution \n" +
          "5.) Exit/Quit the script")
    

def getUserInput():
    # collects users menu option to call appropriate function
    while True:
        printMenu() # prints the menu so user can see choices
        decision = input("Enter a menu option: ")
        if decision == '1': # print the default gateway
            print("The Default Gateway is: " + defaultGateway())
            break
        elif decision == '2': # ping the default gateway
            print(localConnect())
            break
        elif decision == '3': # ping the RIT DNS server address 129.21.3.17
            print(remoteConnect())
            break
        elif decision == '4': # ping www.google.com
            print(dnsRes())
            break
        elif decision == '5': # exit the program
            sys.exit("Quiting")
        else:
            os.system('clear') # clears the terminal before reprinting menu
            print("Input was not valid... Enter a valid menu option")


def defaultGateway():
    # uses the route -n command to and splices the output to print the computers default gateway address
    try:
       DGW = subprocess.run(['route', '-n'], capture_output=True, text=True, check=True)
       output = DGW.stdout.splitlines()

       for line in output:
           if line.startswith('0.0.0.0'): #line in output that contains the default gateway
               tokens = line.split()
               return tokens[1]

    except subprocess.CalledProcessError as error:
        return "Error executing the command" + error
    
    return


def localConnect():
    # uses the ping -c 3 command to ping the default gateway address 3 times and prints the result
    try:
        LC = subprocess.run(['ping', '-c', '3', defaultGateway()], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if LC.returncode == 0: # code 0 = successful ping
            return "The connection was SUCCESSFUL!"
        else:
            return "WARNING... the connection has FAILED"
    
    except Exception as error:
        return "An error has occurred" + error


def remoteConnect():
    # uses the ping -c 3 command to ping the RIT DNS server 3 times and prints the result
    try:
        RC = subprocess.run(['ping', '-c', '3', '129.21.3.17'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if RC.returncode == 0: # code 0 = successful ping
            return "The connection was SUCCESSFUL!"
        else:
            return "WARNING... the connection has FAILED"
    
    except Exception as error:
        return "An error has occurred" + error


def dnsRes():
    # uses nslookup to attempt to reach the www.google.com server and prints the result
    try:
        DNS = subprocess.run(['nslookup', 'www.google.com'], capture_output=True, text=True)

        if DNS.returncode == 0: # code 0 = success in reaching server
            return "The google server is reachable!"
        else:
            return "WARNING... the google server is UNREACHABLE"
        
    except Exception as error:
        return "An error has occured" + error


def main():
    # main function
    while True: #loops until user chooses to exit the program
        getUserInput()
        prompt = input("Run another test? (y/n): ") # I put this in the code so the user can decide how long they want to look at 
        if prompt == 'y':                           # the results instead of immediatly prompting the user for another menu option
            os.system('clear') # clears terminal for new menu
            continue
        else:
            sys.exit("Quiting") # exits the program

if __name__ == "__main__": # for testing
    main() # calls main function