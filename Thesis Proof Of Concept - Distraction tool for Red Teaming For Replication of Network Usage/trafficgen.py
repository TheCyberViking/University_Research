import sys
import socket
import random
import subprocess
import os
from scapy.all import sendp,IP,ICMP,TCP
import secrets

# Install Scapy
# Install TCPreplay

clear = lambda: os.system('clear')

def malwarerun():
    clear()
    malwareans = True
    while malwareans:
        print("This is going to play Traffic of known malware on the network")
        print("This will only work on linux systems")
        print("All traffic will go out eth0")
        print("""
            These are the common Malware Pcaps
            1. Neutrino-EK-traffic
            2. Blackhole-EK-traffic
            3. Nuclear-EK-sends-TeslaCrypt-2.0
            4. malspam-pushing-Dreambot
            5. Emotet-infection-with-Trickbot
            99. Go Back
            """)
        print("")
        ans = input("Which Malware do you want to use: ")
        if ans == "1":
            print("\n Simulating Neutrino-EK-traffic")
            subprocess.call(['sudo', 'tcpreplay','--intf1=eth0', 'malware/1.pcap'])
            print("Simulation Complete")
            malwarerun()

        elif ans == "2":
            print("\n Simulating Blackhole-EK-traffic")
            subprocess.call(['sudo', 'tcpreplay','--intf1=eth0', 'malware/2.pcap'])
            print("Simulation Complete")
            malwarerun()


        elif ans == "3":
            print("\n Simulating Nuclear-EK-sends-TeslaCrypt-2.0")
            subprocess.call(['sudo', 'tcpreplay','--intf1=eth0', 'malware/3.pcap'])
            print("Simulation Complete")
            malwarerun()

        elif ans == "4":
            print("\n Simulating malspam-pushing-Dreambot")
            subprocess.call(['sudo', 'tcpreplay','--intf1=eth0', 'malware/4.pcap'])
            print("Simulation Complete")
            malwarerun()

        elif ans == "5":
            print("\n Simulating Emotet-infection-with-Trickbot")
            subprocess.call(['sudo', 'tcpreplay','--intf1=eth0', 'malware/5.pcap'])
            print("Simulation Complete")
            malwarerun()

        elif ans == "99":
            print("\n Going Back")
            clear()
            replay()

        else:
            print("That is not an option available")
            malwarerun()

def networkattackrun():
    clear()
    netattack = True
    while netattack:
        print("This is going to play Traffic of an attack on the network")
        print("This will only work on linux systems")
        print("All traffic will go out eth0")
        print("""
            These are the Pcaps of Network Attacks
            1. Denial of Service Attack
            2. FTP Crack
            3. OS Finger printeing
            4. Port Scan
            5. CTF "HackChallenge" Traffic
            6. Covert Traffic
            99. Go Back
            """)
        print("")
        ans = input("Which Malware do you want to use: ")
        if ans == "1":
            print("\n Simulating DOS Attack")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'netattacks/dosattack.pcap'])
            print("Simulation Complete")
            networkattackrun()

        elif ans == "2":
            print("\n Simulating FTP Cracl")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'netattacks/ftp-crack.pcap'])
            print("Simulation Complete")
            networkattackrun()


        elif ans == "3":
            print("\n Simulating OS Finger Printing")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'netattacks/osfingerprinting.pcap'])
            print("Simulation Complete")
            networkattackrun()

        elif ans == "4":
            print("\n Simulating Port Scan")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'netattacks/portscan.pcap'])
            print("Simulation Complete")
            networkattackrun()

        elif ans == "5":
            print("\n Simulating A CTF")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'netattacks/HackChallenge_Cmas2010.pcap'])
            print("Simulation Complete")
            networkattackrun()

        elif ans == "6":
            print("\n Simulating Covert Traffic")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'netattacks/covertinfo.pcap'])
            print("Simulation Complete")
            networkattackrun()

        elif ans == "99":
            print("\n Going Back")
            clear()
            menu()

        else:
            print("That is not an option available")
            networkattackrun()

def anonyingtraffic():
    clear()
    anonytrf= True
    while anonytrf:
        print("This is going to play Traffic of an attack on the network")
        print("This will only work on linux systems")
        print("All traffic will go out eth0")
        print("""
            These are the Pcaps of anonying traffic
            1. Barrys Computer Traffic
            2. Beths Computer Traffic
            3. Printer Problems
            99. Go Back
            """)
        print("")
        ans = input("Which Malware do you want to use: ")
        if ans == "1":
            print("\n Simulating Barrys Computer")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'anony/barryscomputer.pcap'])
            print("Simulation Complete")
            anonyingtraffic()

        elif ans == "2":
            print("\n Simulating Beths Computer")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'anony/bethscomputer.pcap'])
            print("Simulation Complete")
            anonyingtraffic()


        elif ans == "3":
            print("\n Simulating Printer Problems")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'anony/printerproblem.pcap'])
            print("Simulation Complete")
            anonyingtraffic()

        elif ans == "99":
            print("\n Going Back")
            replay()

        else:
            print("That is not an option available")
            anonyingtraffic()

def mitminject():
    clear()
    mitm = True
    while mitm:
        print("This is going to play Traffic of an attack on the network")
        print("This will only work on linux systems")
        print("All traffic will go out eth0")
        print("""
            These are the Pcaps of Network Attacks
            1. packetlogic-ttl-localization
            2. hao123-com_packet-injection
            3. id1.cn-inject
            4. id1-cn_packet-injection
            99. Go Back
            """)
        print("")
        ans = input("Which MITM do you want to use: ")
        if ans == "1":
            print("\n Simulating packetlogic-ttl-localization")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'packetinj/1.pcap'])
            print("Simulation Complete")
            mitminject()

        elif ans == "2":
            print("\n Simulating hao123-com_packet-injection")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'packetinj/2.pcap'])
            print("Simulation Complete")
            mitminject()


        elif ans == "3":
            print("\n Simulating id1.cn-inject")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'packetinj/3.pcap'])
            print("Simulation Complete")
            mitminject()

        elif ans == "4":
            print("\n id1-cn_packet-injection")
            subprocess.call(['sudo', 'tcpreplay', '--intf1=eth0', 'packetinj/4.pcap'])
            print("Simulation Complete")
            mitminject()

        elif ans == "99":
            print("\n Going Back")
            replay()

        else:
            print("That is not an option available")
            mitminject()


def replay():
    clear()
    print("This section will allow you to replay a packet on the Network")
    ans = True
    while ans:
        print("")
        print("""
            1. Simulate Malware
            2. Simulate Network Attack
            3. Simulate Anonying Traffic
            4. Simulate MITM Injection Attack
            99. Go back
            """)
        print("")
        ans = input("Choose and Option forom the List: ")
        if ans == "1":
            malwarerun()

        elif ans == "2":
            networkattackrun()


        elif ans == "3":
            anonyingtraffic()

        elif ans == "4":
            mitminject()


        elif ans == "99":
            print("\n Going Back")
            menu()

        else:
            print("!!! please choose a valid menu option, now exiting !!!")
            menu()

def simulateanattack():
    clear()
    ipofvitcim = ".".join(map(str, (random.randint(0, 255)
                                    for _ in range(4))))
    sourcedip = ".".join(map(str, (random.randint(0, 255)
                                    for _ in range(4))))
    portofvictim = random.randint(1,65535)
    mitm = True
    while mitm:
        print("This is going to play Traffic of an attack on the network")
        print("This will only work on linux systems")
        print("All traffic will go out eth0")
        print("""
            These are the Pcaps of Network Attacks this will run as soon as selected ctrl + c to stop
            1. Send Fake Covert Traffic
            2. 
            3. 
            4.  
            99. Go Back
            """)
        print("")
        ans = input("Which Malware do you want to use: ")
        if ans == "1":
            print("\n Sending Fake Covert Traffic")
            print("To Stop you will need to Ctrl + C")
            repeat = True
            while repeat:
                data = secrets.token_bytes(128 // 8)
                packet = IP(src=sourcedip, dst=ipofvitcim,)/TCP(sport=666, dport=portofvictim,)/ data
                sendp(packet, iface="eth0")

        elif ans == "2":
            print("\n Simulating Blackhole-EK-traffic")
            simulateanattack()


        elif ans == "3":
            print("\n Simulating Nuclear-EK-sends-TeslaCrypt-2.0")
            simulateanattack()

        elif ans == "4":
            print("\n Simulating malspam-pushing-Dreambot")
            simulateanattack()

        elif ans == "99":
            print("\n Going Back")
            replay()

        else:
            print("That is not an option available")
            simulateanattack()




def makenois():
    clear()
    print("This will make alot of network noise")
    print("This should flag as unusual traffic")
    print("To Stop This Attack use Ctrl + C ")

    iptoattack = ".".join(map(str, (random.randint(0, 255)
                                    for _ in range(4))))
    porttoattack = random.randint(1,65535)
    noisy = True
    while noisy:
        HOST = iptoattack
        print(iptoattack)
        PORT = porttoattack
        print(porttoattack)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send('GET / HTTP/1.1\r\nHost: pornhub.com\r\n\r\n')

def menu():
    clear()
    ans = True
    while ans:
        print("")
        print("#######################################################")
        print("# Traffic Generator By Dean O'Neill  B00091839        #")
        print("#######################################################")
        print("Please Make sure you run as root and have TCPreplay installed")
        print("")
        print("""
        1. Simulate an Attack
        2. Repaly an Attack
        3. Make noise on the Network
        99. Exit/Quit
        """)
        print("")

        ans = input("Choose and Option from the List: ")
        if ans == "1":
            print("\n Simulating An Attack")
            simulateanattack()

        elif ans == "2":
            print("\n Replay and Attack")
            replay()


        elif ans == "3":
            makenoise()


        elif ans == "99":
            print("\n Closing Program Now")
            sys.exit()

        else:
            print("!!! please choose a vaild menu option, now exiting !!!")
            menu()

# Working Code Bellow
menu()