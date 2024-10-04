#!/usr/bin/python3

# @author Christian Tomassetti
# @nssa221.01
# @script02 assignment
# @project system_report

import os
import subprocess
import platform
import socket

os.system('clear') # clears the terminal for cleaner look

def device_information():
    print("\033[92mDevice Information:\033[0m")
    fqdn = socket.getfqdn()
    hostname = fqdn.split('.')[0]
    domain = '.'.join(fqdn.split('.')[1:])
    print("Hostname:\t\t" + str(hostname))
    print("Domain:\t\t\t" + str(domain))

def network_information():
    print("\033[92mNetwork Information:\033[0m")
    ip_address = socket.gethostbyname(socket.gethostname())
    gateway = subprocess.check_output("ip route | grep default | awk '{print $3}'", shell=True).decode().strip()
    network_mask = subprocess.check_output("ip route | grep kernel | awk '{print $1}'", shell=True).decode().splitlines()[0].strip()
    dns1 = subprocess.check_output("cat /etc/resolv.conf | grep nameserver | awk '{print $2}'", shell=True).decode().splitlines()[0].strip()
    dns2 = subprocess.check_output("cat /etc/resolv.conf | grep nameserver | awk '{print $3}'", shell=True).decode().strip()
    print("IP Address:\t\t" + str(ip_address))
    print("Gateway:\t\t" + str(gateway))
    print("Network Mask:\t\t" + str(network_mask))
    print("DNS1:\t\t\t" + str(dns1))
    if dns2:
        print("DNS2:\t\t\t" + str(dns2))
    else:
        print("\033[91mDNS2:\t\t\tN/A\033[0m")

def system_information():
    print("\033[92mSystem Information:\033[0m")
    
    # Read OS information from /etc/os-release
    os_info = {}
    with open('/etc/os-release') as f:
        for line in f:
            key, value = line.strip().split('=', 1)
            os_info[key] = value.strip('"')
    
    operating_system = os_info.get('PRETTY_NAME', 'Unknown OS')
    os_version = os_info.get('VERSION', 'Unknown Version')
    kernel_version = subprocess.check_output('uname -r', shell=True).decode().strip()
    
    print("Operating System:\t" + str(operating_system))
    print("OS Version:\t\t" + str(os_version))
    print("Kernel Version:\t\t" + str(kernel_version))

def storage_information():
    print("\033[92mStorage Information:\033[0m")
    try:
        root_fs_line = subprocess.check_output("df -h | grep ' /$'", shell=True).decode().strip()
        columns = root_fs_line.split()
        hard_drive_capacity = columns[1]
        available_space = columns[3]
    except subprocess.CalledProcessError as e:
        print("\033[91mError executing command: \033[0m", e)
        hard_drive_capacity = "\033[91mN/A\033[0m"
        available_space = "\033[91mN/A\033[0m"
    
    print("Hard Drive Capacity:\t" + str(hard_drive_capacity))
    print("Available Space:\t" + str(available_space))

def processor_information():
    print("\033[92mProcessor Information:\033[0m")
    cpu_model = subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq | awk '{print $4, $5, $6, $7, $8, $9}'", shell=True).decode().strip()
    num_of_processors = subprocess.check_output("cat /proc/cpuinfo | grep processor | wc -l", shell=True).decode().strip()
    num_of_cores = subprocess.check_output("cat /proc/cpuinfo | grep 'cpu cores' | uniq | awk '{print $4}'", shell=True).decode().strip()
    print("CPU Model:\t\t" + str(cpu_model))
    print("Number of Processors:\t" + str(num_of_processors))
    print("Number of Cores:\t" + str(num_of_cores))

def memory_information():
    print("\033[92mMemory Information:\033[0m")
    total_ram = subprocess.check_output("free -h | grep Mem | awk '{print $2}'", shell=True).decode().strip()
    available_ram = subprocess.check_output("free -h | grep Mem | awk '{print $7}'", shell=True).decode().strip()
    print("Total RAM:\t\t" + str(total_ram))
    print("Available RAM:\t\t" + str(available_ram))

import os

def output_information_to_file():
    file_path = 'system_report.txt'
    
    if os.path.exists(file_path):
        action = input(f"{file_path} already exists. Do you want to (o)verwrite, (a)ppend, or (q)uit? ").strip().lower()
        if action == 'q':
            print("Quitting without writing to the file.")
            return
        elif action == 'a':
            mode = 'a'
        elif action == 'o':
            mode = 'w'
        else:
            print("Invalid option. Quitting without writing to the file.")
            return
    else:
        mode = 'w'
    
    try:
        with open(file_path, mode) as f:
            f.write("Device Information:\n")
            fqdn = socket.getfqdn()
            hostname = fqdn.split('.')[0]
            domain = '.'.join(fqdn.split('.')[1:])
            f.write("Hostname:\t\t" + str(hostname) + "\n")
            f.write("Domain:\t\t\t" + str(domain) + "\n\n")
            
            f.write("Network Information:\n")
            ip_address = socket.gethostbyname(socket.gethostname())
            gateway = subprocess.check_output("ip route | grep default | awk '{print $3}'", shell=True).decode().strip()
            network_mask = subprocess.check_output("ip route | grep kernel | awk '{print $1}'", shell=True).decode().splitlines()[0].strip()
            dns1 = subprocess.check_output("cat /etc/resolv.conf | grep nameserver | awk '{print $2}'", shell=True).decode().splitlines()[0].strip()
            dns2 = subprocess.check_output("cat /etc/resolv.conf | grep nameserver | awk '{print $3}'", shell=True).decode().strip()
            f.write("IP Address:\t\t" + str(ip_address) + "\n")
            f.write("Gateway:\t\t" + str(gateway) + "\n")
            f.write("Network Mask:\t\t" + str(network_mask) + "\n")
            f.write("DNS1:\t\t\t" + str(dns1) + "\n")
            if dns2:
                f.write("DNS2:\t\t\t" + str(dns2) + "\n\n")
            else:
                f.write("DNS2:\t\t\tN/A\n\n")
            
            f.write("System Information:\n")
            os_info = {}
            with open('/etc/os-release') as f_os:
                for line in f_os:
                    key, value = line.strip().split('=', 1)
                    os_info[key] = value.strip('"')
            operating_system = os_info.get('PRETTY_NAME', 'Unknown OS')
            os_version = os_info.get('VERSION', 'Unknown Version')
            kernel_version = subprocess.check_output('uname -r', shell=True).decode().strip()
            f.write("Operating System:\t" + str(operating_system) + "\n")
            f.write("OS Version:\t\t" + str(os_version) + "\n")
            f.write("Kernel Version:\t\t" + str(kernel_version) + "\n\n")
            
            f.write("Storage Information:\n")
            try:
                root_fs_line = subprocess.check_output("df -h | grep ' /$'", shell=True).decode().strip()
                columns = root_fs_line.split()
                hard_drive_capacity = columns[1]
                available_space = columns[3]
            except subprocess.CalledProcessError as e:
                hard_drive_capacity = "N/A"
                available_space = "N/A"
            f.write("Hard Drive Capacity:\t" + str(hard_drive_capacity) + "\n")
            f.write("Available Space:\t" + str(available_space) + "\n\n")
            
            f.write("Processor Information:\n")
            cpu_model = subprocess.check_output("cat /proc/cpuinfo | grep 'model name' | uniq | awk '{print $4, $5, $6, $7, $8, $9}'", shell=True).decode().strip()
            num_of_processors = subprocess.check_output("cat /proc/cpuinfo | grep processor | wc -l", shell=True).decode().strip()
            num_of_cores = subprocess.check_output("cat /proc/cpuinfo | grep 'cpu cores' | uniq | awk '{print $4}'", shell=True).decode().strip()
            f.write("CPU Model:\t\t" + str(cpu_model) + "\n")
            f.write("Number of Processors:\t" + str(num_of_processors) + "\n")
            f.write("Number of Cores:\t" + str(num_of_cores) + "\n\n")
            
            f.write("Memory Information:\n")
            total_ram = subprocess.check_output("free -h | grep Mem | awk '{print $2}'", shell=True).decode().strip()
            available_ram = subprocess.check_output("free -h | grep Mem | awk '{print $7}'", shell=True).decode().strip()
            f.write("Total RAM:\t\t" + str(total_ram) + "\n")
            f.write("Available RAM:\t\t" + str(available_ram) + "\n")
        
        subprocess.run(["xdg-open", file_path])
    except IOError as e:
        print(f"Error writing to file {file_path}: {e}")

def main():
    device_information()
    print('\n')
    network_information()
    print('\n')
    system_information()
    print('\n')
    storage_information()
    print('\n')
    processor_information()
    print('\n')
    memory_information()
    print('\n')
    output_information_to_file()


if __name__ == '__main__':
    main()