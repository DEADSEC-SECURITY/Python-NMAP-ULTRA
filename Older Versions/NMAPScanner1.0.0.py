import nmap
import os
import sys

nm = nmap.PortScanner()

def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():

    global menuoption
    global ipaddr
    global port
    global state
    global portrange

    portrange = "22-1024"

    OS()

    print("Welcome to Python-Nmap Scanner made by DeAdSeC")
    print("----------------------------------------------")
    print("What type of scan would you like to run?")
    print("1) Full Network Scan")
    print("2) TPC Scan")
    print("3) UDP Scan")
    print("4) Scan for a specified port")

    menuoption = int(input())

    if menuoption == 1:
        OS()
        ipaddr = input("Please enter your ip address: ")

        nm.scan(ipaddr, portrange, '-v')

        OS()
        print("Colected data:")
        print("--------------")
        print("Ip Status: ", nm[ipaddr].state())
        print("Port Range: ", portrange)
        print("HostName: ", nm[ipaddr].hostname())
        print("Scanned Hosts: ", nm.all_hosts())
        print("Open TCP Ports: ", nm[ipaddr].all_tcp())
        print("Open UDP Ports: ", nm[ipaddr].all_udp())
        print("Open SCTP Ports: ", nm[ipaddr].all_sctp())
        print("Open IP Ports: ", nm[ipaddr].all_ip())
        sys.exit()

    if menuoption == 2:

        OS()
        ipaddr = input("Please enter your ip address: ")

        nm.scan(ipaddr, portrange, '-v')

        OS()
        print("Colected data:")
        print("--------------")
        print("Ip Status: ", nm[ipaddr].state())
        print("Port Range: ", portrange)
        print("HostName: ", nm[ipaddr].hostname())
        print("Scanned Hosts: ", nm.all_hosts())
        print("Open TCP Ports: ", nm[ipaddr].all_tcp())
        sys.exit()

    if menuoption == 3:
        OS()
        ipaddr = input("Please enter your ip address: ")

        nm.scan(ipaddr, portrange, '-v')

        OS()
        print("Colected data:")
        print("--------------")
        print("Ip Status: ", nm[ipaddr].state())
        print("Port Range: ", portrange)
        print("HostName: ", nm[ipaddr].hostname())
        print("Scanned Hosts: ", nm.all_hosts())
        print("Open UDP Ports: ", nm[ipaddr].all_udp())
        sys.exit()

    if menuoption == 4:
        OS()
        ipaddr = input("Please enter your ip address: ")

        OS()
        port = input("Please enter the port you wanna scan: ")

        nm.scan(ipaddr, portrange, '-v')

        OS()
        print("Colected data:")
        print("--------------")
        print("Ip Status: ", nm[ipaddr].state())
        print("Selected Port: ", port)
        print("HostName: ", nm[ipaddr].hostname())
        print("Scanned Hosts: ", nm.all_hosts())
        print("UDP OPEN: ", nm[ipaddr].has_udp(int(port)))
        print("TCP OPEN: ", nm[ipaddr].has_tcp(int(port)))
        print("SCTP OPEN: ", nm[ipaddr].has_sctp(int(port)))
        sys.exit()

    else:
        OS()
        print("You fucked up a simple shit!")
        return menu()


menu()
