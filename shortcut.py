#!/usr/bin/python3

# Author: Christian Tomassetti
# NSSA221.01
# Script03 Assignment
# Project: Symbolic Links

import os
import sys
from datetime import datetime
from pathlib import Path
import subprocess

os.system('clear')  # clears the terminal for cleaner look

def stamp():
    # Display the date and time
    time_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\033[91mSystem Report - {time_date}\033[0m")

def find_files(query):
    # Find files matching the query and suppress errors
    result = []
    try:
        # Using find command to search for files
        command = f"find / -name '{query}' 2>/dev/null"
        print(f"\033[93mRunning command: {command}\033[0m")  # Debug output
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT).decode().strip().split('\n')
        print(f"\033[93mRaw output: {output}\033[0m")  # Debug output
        result = [line for line in output if line and os.path.exists(line)]
    except subprocess.CalledProcessError as e:
        print("\033[91mAn error occurred while searching for files.\033[0m")
        print(e.output.decode())

    return result

def create_symlink():
    # Create a symbolic link
    print("\033[92mCreate a Symbolic Link:\033[0m")
    print("Enter the name of the file or directory you would like to create a symbolic link for:")
    file_name = input().strip()
    
    # Find matching files
    matches = find_files(file_name)
    
    if not matches:
        print(f"\033[91mNo matches found for '{file_name}'.\033[0m")
        return

    print("\033[93mMatches found:\033[0m")
    for index, match in enumerate(matches):
        print(f"{index + 1}: {match}")

    try:
        choice = int(input("Select the number corresponding to the file/directory you want to link: "))
        if choice < 1 or choice > len(matches):
            raise ValueError
    except ValueError:
        print("\033[91mInvalid selection.\033[0m")
        return

    target_path = matches[choice - 1]
    desktop_path = Path(os.path.expanduser('~/Desktop'))
    symlink_path = desktop_path / Path(target_path).name

    # Handle pre-existing symbolic links
    if symlink_path.exists():
        print(f"\033[91m{symlink_path.name} already exists on the Desktop.\033[0m")
        return

    os.symlink(target_path, symlink_path)
    print(f"\033[92mSymbolic link to '{target_path}' created on the Desktop as '{symlink_path.name}'.\033[0m")

def delete_symlink():
    # Delete a symbolic link
    print("\033[92mDelete a Symbolic Link:\033[0m")
    print("Enter the file name you would like to delete the symbolic link for:")
    file_name = input().strip()
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