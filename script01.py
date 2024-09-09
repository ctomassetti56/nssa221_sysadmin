#!/usr/bin/python3
import os
import subprocess
import sys

def printMenu():
    print("1.) Display the default gateway \n" +
          "2.) Test Local Connectivity \n" +
          "3.) Test Remote Connectivity \n" +
          "4.) Test DNS Resolution \n" +
          "5.) Exit/Quit the script")
    
def getUserInput():
    while True:
        printMenu()
        decision = input("Enter a menu option: ")
        intDecision = int(decision)
        if intDecision >= 1 and intDecision <= 5:
            if intDecision == 1:
                defaultGateway()
                break
            elif intDecision == 2:
                localConnect()
                break
            elif intDecision == 3:
                remoteConnect()
                break
            elif intDecision == 4:
                dnsRes()
                break
            elif intDecision == 5:
                sys.exit("Quiting")
        else:
            os.system('clear')
            print("Input was not valid... Enter a valid menu option")

def defaultGateway():
    try:
       result = subprocess.run(['route', '-n'], capture_output=True, text=True, check=True)
       output = result.stdout.splitlines()

       for line in output:
           if line.startswith('0.0.0.0'):
               tokens = line.split()
               return tokens[1]

    except subprocess.CalledProcessError as error:
        print(f"Error executing command: {error}")
    return

def localConnect():
    return

def remoteConnect():
    return

def dnsRes():
    return

def main():
    getUserInput()


if __name__ == "__main__":
    main()