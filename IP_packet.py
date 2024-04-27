from scapy.all import *
import subprocess

#IP packet handler

ipDST = sys.argv[1]
ip = IP()

########################IP Address Testing##########################

test = subprocess.check_output(['python.exe','./ipTest.py',ipDST])

match int(test):
    case 0:
        print("Error: Bad IP Address")
        sys.exit()
    case 4:
        ip = IP(dst=ipDST)
    case 6:
        ip = IPv6(dst=ipDST)
    case _:
        print("Error: Unknown IP Error")

####################################################################

packet = ip
send(packet)

