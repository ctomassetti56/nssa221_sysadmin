#!/usr/bin/python3

# @author Christian Tomassetti
# @nssa221.01
# @script03 assignment
# @project symbolic_links

import os
import sys
import datetime
from pathlib import Path

os.system('clear') # clears the terminal for cleaner look

def stamp():
    # Display the date and time
    time_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\033[91mSystem Report - {time_date}\033[0m")

def create_symlink():
    # Create a symbolic link
    print("\033[92mCreate a Symbolic Link:\033[0m")
    print("Enter the file name you would like to create a symbolic link for:")
    file_name = input()
    file_path = Path(f"{os.path.expanduser('~')}/Desktop/{file_name}")
    if file_path.exists():
        print(f"\033[91m{file_name} already exists on the Desktop.\033[0m")
    else:
        print("Enter the target path for the symbolic link:")
        target_path = input()
        os.symlink(target_path, file_path)
        print(f"\033[92m{file_name} symbolic link created on the Desktop.\033[0m")
    
def delete_symlink():
    # Delete a symbolic link
    print("\033[92mDelete a Symbolic Link:\033[0m")
    print("Enter the file name you would like to delete the symbolic link for:")
    file_name = input()
    file_path = Path(f"{os.path.expanduser('~')}/Desktop/{file_name}")
    if file_path.exists():
        os.remove(file_path)
        print(f"\033[92m{file_name} symbolic link deleted from the Desktop.\033[0m")
    else:
        print(f"\033[91m{file_name} does not exist on the Desktop.\033[0m")

def report_symlinks():
    # Run a report summarizing the symbolic links on the user's desktop
    print("\033[92mSymbolic Link Report:\033[0m")
    desktop_path = Path(f"{os.path.expanduser('~')}/Desktop")
    for file in desktop_path.iterdir():
        if file.is_symlink():
            print(f"{file.name} -> {os.readlink(file)}")

def main():
    while True:
        print("\033[92mMenu:\033[0m")
        print("1. Create a Symbolic Link")
        print("2. Delete a Symbolic Link")
        print("3. Run a Report")
        print("4. Exit")
        choice = input("Enter an option: ")
        if choice == '1':
            create_symlink()
            os.system('clear') # clears the terminal for cleaner look
        elif choice == '2':
            delete_symlink()
        elif choice == '3':
            report_symlinks()
        elif choice == '4':
            sys.exit()
        else:
            print("\033[91mInvalid option. Please try again.\033[0m")

if __name__ == "__main__":
    stamp()
    main()