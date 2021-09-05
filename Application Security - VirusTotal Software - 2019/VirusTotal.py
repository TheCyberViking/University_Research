from virustotal_python import Virustotal
import datetime
import time
import hashlib
from os import system, name
import json


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def main():
    print("Code Currently Only Works on Windows with python 3.7")
    print("Wrote By Dean B0009 for Application Security 2019/2020")
    print("")
    print("The Current Time is:")
    print(utc)
    print("Each Section Will Generate its own Report")
    print("""
        1.Scan a File
        2.Scan a URL
        3.Search a Hash
        4.Scan an IP
        5.Report Status
        """)
    answer = input("What would you like to do? use numbers to select: ")
    if answer == "1":
        scanfile()
    elif answer == "2":
        scanurl()
    elif answer == "3":
        hashsearch()
    elif answer == "4":
        searchip()
    elif answer == "5":
        reportstatus()
    elif answer != "":
        print("\n Not Valid Choice Try again")
        main()


def scanfile():
    print("")
    # this will take a file check its hash, if its hash isnt found it will upload the sample
    print("This Will scan files for possible viruses")
    print("")
    print("Please set as Filename.blah this can be done by dragging the file into the console")
    filename = input("Please give file location: ")
    print("\nThe file is set to: " + filename)
    responsefromvt = vtotal.file_scan(filename)
    md5h = sha256sum(filename)
    print("Files Sha256 hash: " + md5h)
    time.sleep(20)
    print("Scanning the File Now, this may take a few second")
    responsefromvt = vtotal.file_report([md5h])
    print("")
    print("Generating Report Now")
    print("This Will Creat a HTML File with the report data")
    utc1 = str(utc).replace(':', '_')
    f = open(str(utc1) + "_" + 'ScannedFile' + ".json", "w+")
    f.write(str(json.dumps(responsefromvt, sort_keys=False, indent=4)))
    f.close()
    print("Returning to Main Menu after File Created")
    print("")
    time.sleep(5)
    clear()
    main()


# This code section was built with help from https://stackoverflow.com/questions/22058048/hashing-a-file-in-python
def sha256sum(filename):
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


def scanurl():
    print("")
    print("This will scan a URL for issues")
    print("in format sample.com")
    urltoscan = input("What URL do you want to scan: ")
    responsefromvt = vtotal.url_scan(urltoscan)
    time.sleep(10)
    print("Scanning the File Now, this may take a second")
    responsefromvt = vtotal.url_report(urltoscan)
    responsefromvt = vtotal.domain_report(urltoscan)
    print("")
    print("Generating Report Now")
    print("This Will Creat a HTML File with the report data")
    utc1 = str(utc).replace(':', '_')
    f = open(str(utc1) + "_" + urltoscan + ".json", "w+")
    f.write(str(json.dumps(responsefromvt, sort_keys=False, indent=4)))
    f.close()
    print("Returning to Main Menu after File Created")
    print("")
    time.sleep(5)
    clear()
    main()


def hashsearch():
    print("")
    print("This will Allow you to search a Hash")
    hashtosearch = input("Please insert the MD5 / SHA1 / SHA256 Hash: ")
    responsefromvt = vtotal.file_rescan
    time.sleep(10)
    responsefromvt = vtotal.file_report([hashtosearch])
    print("")
    print("Generating Report Now")
    print("This Will Creat a HTML File with the report data")
    utc1 = str(utc).replace(':', '_')
    f = open(str(utc1) + "_" + 'HashSearch' + ".json", "w+")
    f.write(str(json.dumps(responsefromvt, sort_keys=False, indent=4)))
    f.close()
    print("Returning to Main Menu after File Created")
    print("")
    time.sleep(5)
    clear()
    main()


def searchip():
    print("")
    print("This will Allow you to search a IP Address")
    iptosearch = input("Please Input IP to Search: ")
    responsefromvt = vtotal.ipaddress_report(iptosearch)
    # time.sleep(10)
    print("Scanning the File Now, this may take a second")
    print("")
    print("Generating Report Now")
    print("This Will Creat a HTML File with the report data")
    # For troubleShooting json output
    # print(json.dumps(responsefromvt, sort_keys=False, indent=4))
    utc1 = str(utc).replace(':', '_')
    f = open(str(utc1) + "_" + iptosearch + ".json", "w+")
    f.write(str(json.dumps(responsefromvt, sort_keys=False, indent=4)))
    f.close()
    print("Returning to Main Menu after File Created")
    print("")
    time.sleep(5)
    clear()
    main()


def reportstatus():
    print("")
    print("This section will show current report status")
    print("Hash Format Accepted Sha256")
    status = input("Please Enter your Has to Search: ")
    print("")
    responsefromvt = vtotal.file_report([status])
    print(json.dumps(responsefromvt, sort_keys=False, indent=4))
    time.sleep(20)
    main()


vtotal = Virustotal("1889b1ae9287d8d3f55ab4e4ab0baa501849cfa09d55dd30021a317c35a64f6d")
utc = datetime.datetime.now().time()
main()
