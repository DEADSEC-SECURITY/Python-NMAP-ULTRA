#-----------Welcome to DeAdSeC Python Nmap Scanner----------#
#-------Made By DeAdSeC-------#
#---Version 2.1.1---#

import nmap
import os
import sys
import json
import logging

nm = nmap.PortScanner()

def OS():
    os.system('cls' if os.name == 'nt' else 'clear')

def Scan():

    global state
    global host
    global scanned_hosts
    global All_IP
    global All_TCP
    global All_UDP
    global All_SCTP
    global Has_TCP
    global Has_UPD
    global Has_SCTP

    #Will make a scan of the network and organise the info in string!
    nm.scan(defaultipaddr, portrange, '-v')

    state = nm[defaultipaddr].state()
    host = nm[defaultipaddr].hostname()
    scanned_hosts = str(nm.all_hosts())
    All_TCP = str(nm[defaultipaddr].all_tcp())
    All_UDP = str(nm[defaultipaddr].all_udp())
    All_SCTP = str(nm[defaultipaddr].all_sctp())
    All_IP = str(nm[defaultipaddr].all_ip())

def FullNetworkScan():

    #Will run Scan function so it can organize print and log all the info!
    Scan()

    OS()

    #Will print the data colected

    print("Colected data:")
    print("--------------")
    print("Ip Status: " + state)
    print("Port Range: " + portrange)
    print("HostName: " + host)
    print("Scanned Hosts: " + scanned_hosts)
    print("Open TCP Ports: " + All_TCP)
    print("Open UDP Ports: " + All_UDP)
    print("Open SCTP Ports: " + All_SCTP)
    print("Open IP Ports: " + All_IP)

    #Will create logs of all commands ran

    logging.info("")
    logging.info("")
    logging.info("ALL DATA COLECTED FROM A FULL SCAN")
    logging.info("Colected data:")
    logging.info("--------------")
    logging.info("Ip Status: " + state)
    logging.info("Port Range: " + portrange)
    logging.info("HostName: " + host)
    logging.info("Scanned Hosts " + scanned_hosts)
    logging.info("Open TCP Ports: " + All_TCP)
    logging.info("Open UDP Ports: " + All_UDP)
    logging.info("Open SCTP Ports: " + All_SCTP)
    logging.info("Open IP Ports: " + All_IP)

    print()
    input("Press any key to continue! ")
    menu()

def TCPScan():

    Scan()

    OS()

    #Will print the data colected!

    print("Colected data:")
    print("--------------")
    print("Ip Status: " + state)
    print("Port Range: " + portrange)
    print("HostName: " + host)
    print("Scanned Hosts: " + scanned_hosts)
    print("Open TCP Ports: " + All_TCP)

    #Will log the data colected!

    logging.info("")
    logging.info("")
    logging.info("ALL DATA COLECTED FROM A TCP SCAN")
    logging.info("Colected data:")
    logging.info("--------------")
    logging.info("Ip Status: " + state)
    logging.info("Port Range: " + portrange)
    logging.info("HostName: " + host)
    logging.info("Scanned Hosts " + scanned_hosts)
    logging.info("Open TCP Ports: " + All_TCP)

    print()
    input("Press any key to continue! ")
    menu()

def UDPScan():

    Scan()

    OS()

    #Will print all the info colected

    print("Colected data:")
    print("--------------")
    print("Ip Status: ", nm[defaultipaddr].state())
    print("Port Range: ", portrange)
    print("HostName: ", nm[defaultipaddr].hostname())
    print("Scanned Hosts: ", nm.all_hosts())
    print("Open UDP Ports: ", nm[defaultipaddr].all_udp())

    #Will create logs of all commands ran

    logging.info("")
    logging.info("")
    logging.info("ALL DATA COLECTED FROM A UDP SCAN")
    logging.info("Colected data:")
    logging.info("--------------")
    logging.info("Ip Status: " + state)
    logging.info("Port Range: " + portrange)
    logging.info("HostName: " + host)
    logging.info("Scanned Hosts " + scanned_hosts)
    logging.info("Open UDP Ports: " + All_UDP)

    print()
    input("Press any key to continue! ")
    menu()

def SpecificPort():

    Scan()

    Has_TCP = str(nm[defaultipaddr].has_tcp(int(port)))
    Has_UPD = str(nm[defaultipaddr].has_udp(int(port)))
    Has_SCTP = str(nm[defaultipaddr].has_sctp(int(port)))

    OS()

    #Will print the info colected!

    print("Colected data:")
    print("--------------")
    print("Ip Status: " + state)
    print("Selected Port: " + port)
    print("HostName: " + host)
    print("Scanned Hosts: " + scanned_hosts)
    print("UDP OPEN: " + Has_UPD)
    print("TCP OPEN: " + Has_TCP)
    print("SCTP OPEN: " + Has_SCTP)

    #Will create logs of all commands ran!

    logging.info("")
    logging.info("")
    logging.info("ALL DATA COLECTED FROM A Specific Port SCAN")
    logging.info("Colected data:")
    logging.info("--------------")
    logging.info("Ip Status: " + state)
    logging.info("Port Range: " + portrange)
    logging.info("HostName: " + host)
    logging.info("Scanned Hosts " + scanned_hosts)
    logging.info("UDP OPEN: " + Has_UPD)
    logging.info("TCP OPEN: " + Has_TCP)
    logging.info("SCTP OPEN: " + Has_SCTP)

    print()
    input("Press any key to continue! ")
    menu()

def Logs():
    logging.basicConfig(filename = 'LOGS/LOG', level = logging.INFO,
                        format = '%(asctime)s:%(message)s')

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
    global my_date

    Logs()

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
    print("2) TCP Scan")
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
        newip = input("Please enter your new default ip address: ")
        data['DataInfo'][0]['defaultipaddress'] = defaultipaddr = newip
        with open('Data/DATA.json', 'w') as f:
            json.dump(data, f, indent = 2)

        OS()
        print("Default ip address changed to " + newip)

        logging.info("Port range changed to " + newip)
        sys.exit()

    if menuoption == 6:

        OS()
        newport = input("Please enter your new default port range: ")
        data['DataInfo'][0]['defaultportrange'] = portrange = newport
        with open('Data/DATA.json', 'w') as f:
            json.dump(data, f, indent = 2)

        OS()
        print("Default port range changed to " + newport)

        logging.info("Port range changed to " + newport)
        sys.exit()

    else:
        OS()
        print("You fucked up a simple shit!")
        return menu()


menu()
