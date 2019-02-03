#-----------Welcome to DeAdSeC Python Nmap Scanner----------#
#-------Made By DeAdSeC-------#
#---Version 2.0.0---#

import nmap
import os
import sys
import json

nm = nmap.PortScanner()

def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

def FullNetworkScan():

    nm.scan(defaultipaddr, portrange, '-v')

    OS()
    print("Colected data:")
    print("--------------")
    print("Ip Status: ", nm[defaultipaddr].state())
    print("Port Range: ", portrange)
    print("HostName: ", nm[defaultipaddr].hostname())
    print("Scanned Hosts: ", nm.all_hosts())
    print("Open TCP Ports: ", nm[defaultipaddr].all_tcp())
    print("Open UDP Ports: ", nm[defaultipaddr].all_udp())
    print("Open SCTP Ports: ", nm[defaultipaddr].all_sctp())
    print("Open IP Ports: ", nm[defaultipaddr].all_ip())
    sys.exit()

def TCPScan():

    nm.scan(defaultipaddr, portrange, '-v')

    OS()
    print("Colected data:")
    print("--------------")
    print("Ip Status: ", nm[defaultipaddr].state())
    print("Port Range: ", portrange)
    print("HostName: ", nm[defaultipaddr].hostname())
    print("Scanned Hosts: ", nm.all_hosts())
    print("Open TCP Ports: ", nm[defaultipaddr].all_tcp())
    sys.exit()

def UDPScan():

    nm.scan(defaultipaddr, portrange, '-v')

    OS()
    print("Colected data:")
    print("--------------")
    print("Ip Status: ", nm[defaultipaddr].state())
    print("Port Range: ", portrange)
    print("HostName: ", nm[defaultipaddr].hostname())
    print("Scanned Hosts: ", nm.all_hosts())
    print("Open UDP Ports: ", nm[defaultipaddr].all_udp())
    sys.exit()

def SpecificPort():

    nm.scan(defaultipaddr, portrange, '-v')

    OS()
    print("Colected data:")
    print("--------------")
    print("Ip Status: ", nm[defaultipaddr].state())
    print("Selected Port: ", port)
    print("HostName: ", nm[defaultipaddr].hostname())
    print("Scanned Hosts: ", nm.all_hosts())
    print("UDP OPEN: ", nm[defaultipaddr].has_udp(int(port)))
    print("TCP OPEN: ", nm[defaultipaddr].has_tcp(int(port)))
    print("SCTP OPEN: ", nm[defaultipaddr].has_sctp(int(port)))
    sys.exit()

def menu():

    global menuoption
    global ipaddr
    global port
    global state
    global portrange
    global defaultipaddr
    global optionip
    global optionport
    global newip
    global newport

    with open('Data/DATA.json') as f:
        data = json.load(f)

    for DataInfo in data['DataInfo']:
        portrange = DataInfo['defaultportrange']
        defaultipaddr = DataInfo['defaultipaddress']

    OS()

    print("Welcome to Python-Nmap Scanner made by DeAdSeC")
    print("----------------------------------------------")
    print("What type of scan would you like to run?")
    print("1) Full Network Scan")
    print("2) TPC Scan")
    print("3) UDP Scan")
    print("4) Scan for a specified port")
    print("------------")
    print("5) Change default ip address")
    print("6) Change default port range")
    print("-----------")

    #print("\033[1;32;40mWelcome to Python-Nmap Scanner made by DeAdSeC")
    #print("\033[1;36;40m----------------------------------------------")
    #print("\033[1;36;40mWhat type of scan would you like to run?")
    #print("\033[1;36;40m1) Full Network Scan")
    #print("\033[1;36;40m2) TPC Scan")
    #print("\033[1;36;40m3) UDP Scan")
    #print("\033[1;37;40m------------")
    #print("\033[1;36;40m4) Scan for a specified port")
    #print("\033[1;36;40m5) Change default ip address")
    #print("\033[1;36;40m6) Change default port range")
    #print("\033[1;37;40m-----------")

    menuoption = int(input())

    if menuoption == 1:
        OS()
        print("Would you like to use the default ip? [" + defaultipaddr + "]")
        optionip = input()

        if optionip == "Y":

            OS()
            print("Would you like to use the default port range? [" + portrange + "]")
            optionport = input()

            if optionport == "Y":

                return FullNetworkScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return FullNetworkScan()

            if optionport == "y":

                return FullNetworkScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return FullNetworkScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "N":

            OS()
            defaultipaddr = input("Please enter your ip address: ")

            OS()
            print("Would you like to use the default port range? [", portrange, "]")
            optionport = input()

            if optionport == "Y":

                return FullNetworkScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return FullNetworkScan()

            if optionport == "y":

                return  FullNetworkScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return FullNetworkScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "y":

            OS()
            print("Would you like to use the default port range? [" + portrange + "]")
            optionport = input()

            if optionport == "Y":

                nm.scan(ipaddr, portrange, '-v')

                return FullNetworkScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return FullNetworkScan()

            if optionport == "y":

                return FullNetworkScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return FullNetworkScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "n":

            OS()
            defaultipaddr = input("Please enter your ip address: ")

            OS()
            print("Would you like to use the default port range? [", portrange, "]")
            optionport = input()

            if optionport == "Y":

                return FullNetworkScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return FullNetworkScan()

            if optionport == "y":

                return FullNetworkScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return FullNetworkScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        else:
            print("Use only Y/N or y/n")
            return menu()

    if menuoption == 2:

        OS()
        print("Would you like to use the default ip? [" + defaultipaddr + "]")
        optionip = input()

        if optionip == "Y":

            OS()
            print("Would you like to use the default port range? [" + portrange + "]")
            optionport = input()

            if optionport == "Y":

                return TCPScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return TCPScan()

            if optionport == "y":

                return TCPScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return TCPScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "N":

            OS()
            defaultipaddr = input("Please enter your ip address: ")

            OS()
            print("Would you like to use the default port range? [", portrange, "]")
            optionport = input()

            if optionport == "Y":

                return TCPScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return TCPScan()

            if optionport == "y":

                return  TCPScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return TCPScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "y":

            OS()
            print("Would you like to use the default port range? [" + portrange + "]")
            optionport = input()

            if optionport == "Y":

                nm.scan(ipaddr, portrange, '-v')

                return FTCPScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return TCPScan()

            if optionport == "y":

                return TCPScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return TCPScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "n":

            OS()
            defaultipaddr = input("Please enter your ip address: ")

            OS()
            print("Would you like to use the default port range? [", portrange, "]")
            optionport = input()

            if optionport == "Y":

                return TCPScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return TCPScan()

            if optionport == "y":

                return TCPScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return TCPScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        else:
            print("Use only Y/N or y/n")
            return menu()

    if menuoption == 3:

        OS()
        print("Would you like to use the default ip? [" + defaultipaddr + "]")
        optionip = input()

        if optionip == "Y":

            OS()
            print("Would you like to use the default port range? [" + portrange + "]")
            optionport = input()

            if optionport == "Y":

                return UDPScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return UDPScan()

            if optionport == "y":

                return UDPScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return UDPScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "N":

            OS()
            defaultipaddr = input("Please enter your ip address: ")

            OS()
            print("Would you like to use the default port range? [", portrange, "]")
            optionport = input()

            if optionport == "Y":

                return UDPScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return UDPScan()

            if optionport == "y":

                return  UDPScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return UDPScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "y":

            OS()
            print("Would you like to use the default port range? [" + portrange + "]")
            optionport = input()

            if optionport == "Y":

                nm.scan(ipaddr, portrange, '-v')

                return UDPScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return UDPScan()

            if optionport == "y":

                return UDPScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return UDPScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        if optionip == "n":

            OS()
            defaultipaddr = input("Please enter your ip address: ")

            OS()
            print("Would you like to use the default port range? [", portrange, "]")
            optionport = input()

            if optionport == "Y":

                return UDPScan()

            if optionport == "N":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return UDPScan()

            if optionport == "y":

                return UDPScan()

            if optionport == "n":

                OS()
                print("Please use this format for the port range: MinPort-MaxPort")
                portrange = input("What port range would you want me to use: ")

                return UDPScan()

            else:
                print("Please use only Y/N or y/n")
                return menu()

        else:
            print("Use only Y/N or y/n")
            return menu()

    if menuoption == 4:
        OS()
        print("Would you like to use the default ip? [" + defaultipaddr + "]")
        optionip = input()

        OS()
        port = input("Please enter the port you wanna scan: ")

        if optionip == "Y":

            return  SpecificPort()

        if optionip == "N":

            OS()
            defaultipaddr = input("Please enter your ip address: ")

            return SpecificPort()

        if optionip == "y":

            return SpecificPort()

        if optionip == "n":

            OS()
            defaultipaddr = input("Please enter your ip address: ")

            return SpecificPort()

    if menuoption == 5:

        OS()
        newip = input("NOT IMPLEMENTER")
        return menu()

    if menuoption == 6:
        OS()
        newip = input("NOT IMPLEMENTER")
        return menu()

    else:
        OS()
        print("You fucked up a simple shit!")
        return menu()


menu()
