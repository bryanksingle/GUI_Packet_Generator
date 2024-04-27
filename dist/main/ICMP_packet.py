from scapy.all import *

#ICMP packet handler

ipAddr = str(sys.argv[1])

test = subprocess.check_output(['python.exe','./ipTest.py',ipAddr])

match int(test):
    case 0:
        print("Error: Bad IP Address")
        sys.exit()
    case 4:
        ip = IP(dst=ipAddr)
        icmp = ICMP(type = int(sys.argv[2]))
    case 6:
        ip = IPv6(dst=ipAddr)
        match int(sys.argv[2]):
            case 133:
                icmp = ICMPv6ND_RS()
            case 134:
                icmp = ICMPv6ND_RA()
            case 135:
                icmp = ICMPv6ND_NS()
            case 136:
                icmp = ICMPv6ND_NA()
            case 137:
                icmp = ICMPv6ND_Redirect()
            case _:
                print("Error: Invaid Type Code")
                sys.exit()
    case _:
        print("Error: Unknown IP Error")
        sys.exit()

packet = ip / icmp

send(packet)





