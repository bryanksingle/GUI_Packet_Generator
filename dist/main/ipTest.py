from scapy.all import *
import ipaddress

#IP Address Test

tSwitch = False

ipDST = sys.argv[1]
try:
    check = ipaddress.IPv4Address(ipDST)
    
    tSwitch = True
    print("4")
    sys.exit()
except:
    pass
if(tSwitch == False):
    try:
        check = ipaddress.IPv6Address(ipDST)
        
        tSwitch = True
        print("6")
        sys.exit()
    except:
        pass

if(tSwitch == False):
    print("0")
    sys.exit()



