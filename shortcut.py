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
    # Find files matching the query using os.walk
    result = []
    for root, dirs, files in os.walk('/'):
        for name in files + dirs:
            if query in name:
                result.append(os.path.join(root, name))
    return result

def create_symlink():
    os.system('clear')  # clears the terminal for cleaner look
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
        # Clear the terminal after the user makes a selection
        os.system('clear')
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
        action = input(f"\033[91m{symlink_path.name} already exists on the Desktop. Do you want to (o)verwrite, (s)kip, or (r)ename? ").strip().lower()
        if action == 'o':
            os.remove(symlink_path)
        elif action == 's':
            print("\033[91mSkipping creation of symbolic link.\033[0m")
            return
        elif action == 'r':
            new_name = input("Enter the new name for the symbolic link: ").strip()
            symlink_path = desktop_path / new_name
        else:
            print("\033[91mInvalid option. Skipping creation of symbolic link.\033[0m")
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