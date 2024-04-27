from scapy.all import *

#TCP packet handler

ipDST = sys.argv[1]
srcPort = sys.argv[2]
dstPort = sys.argv[3]
data = Raw(load=sys.argv[4])

if (len(sys.argv)<6):
    theFlags = ''
else:
    theFlags = sys.argv[5]

#############################Error checking##################################

try:
    int(srcPort)
    int(dstPort)
except ValueError:
    print("Error: Port(s) Not Integer")
    sys.exit()

if(((int(srcPort)) < 0) or ((int(srcPort)) > 65535) ):
    print("Error: Source Port Out of Range (0-65535)")
    sys.exit()

if(((int(dstPort)) < 0) or ((int(dstPort)) > 65535) ):
    print("Error: Destination Port Out of Range (0-65535)")
    sys.exit()

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

#############################################################################

tcp = TCP(sport = int(srcPort), dport = int(dstPort), flags = theFlags)

packet = ip/tcp/data

send(packet)
