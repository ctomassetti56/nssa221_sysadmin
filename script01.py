#!/usr/bin/python3
import os
import subprocess
import sys

os.system('clear')

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
        if decision == '1':
            print(defaultGateway())
            break
        elif decision == '2':
            print(localConnect())
            break
        elif decision == '3':
            print(remoteConnect())
            break
        elif decision == '4':
            dnsRes()
            break
        elif decision == '5':
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
    return
    

def main():
    while True:
        getUserInput()
        os.system('clear')


if __name__ == "__main__":
    main()