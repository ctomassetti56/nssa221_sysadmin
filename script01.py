#!/usr/bin/python3
import os
import subprocess
import sys

os.system('clear') #clears the terminal for cleaner look

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
        printMenu() #prints the menu so user can see choices
        decision = input("Enter a menu option: ")
        if decision == '1': # print the default gateway
            print(defaultGateway())
            break
        elif decision == '2': # ping the loopback address 127.0.0.1
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
            os.system('clear')
            print("Input was not valid... Enter a valid menu option")


def defaultGateway():
    try:
       DGW = subprocess.run(['route', '-n'], capture_output=True, text=True, check=True)
       output = DGW.stdout.splitlines()

       for line in output:
           if line.startswith('0.0.0.0'):
               tokens = line.split()
               return tokens[1]

    except subprocess.CalledProcessError as error:
        return "Error executing the command" + error
    
    return


def localConnect():
    try:
        loopBack = subprocess.run(['ping', '-c', '3', '127.0.0.1'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if loopBack.returncode == 0:
            return "The connection was SUCCESSFUL!"
        else:
            return "WARNING... the connection has FAILED"
    
    except Exception as error:
        return "An error has occurred" + error


def remoteConnect():
    try:
        RC = subprocess.run(['ping', '-c', '3', '129.21.3.17'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if RC.returncode == 0:
            return "The connection was SUCCESSFUL!"
        else:
            return "WARNING... the connection has FAILED"
    
    except Exception as error:
        return "An error has occurred" + error


def dnsRes():
    try:
        DNS = subprocess.run(['nslookup', 'www.google.com'], capture_output=True, text=True)

        if DNS.returncode == 0:
            return "The google server is reachable!"
        else:
            return "WARNING... the google server is UNREACHABLE"
        
    except Exception as error:
        return "An error has occured" + error


def main():
    while True:
        getUserInput()
        prompt = input("Run another test? (y/n): ")
        if prompt == 'y':
            os.system('clear')
            continue
        else:
            sys.exit("Quiting")

if __name__ == "__main__":
    main()