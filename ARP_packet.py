from scapy.all import *

#ARP packet handler

ipAddr = str(sys.argv[1])
toggle = sys.argv[2]

#############################IP Address Testing#####################################

test = subprocess.check_output(['python.exe','./ipTest.py',ipAddr])
match int(test):

    case 4:
        pass
    case 6:
        print("Error:+ARP+Does+Not+Support+IPv6")
        sys.exit()
    case _:
        print("Error:+Bad+IP")
        sys.exit()

##############################################################################

packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst = ipAddr)

if(toggle=='False'):
        response = sendp(packet)
        sys.exit()
    

response = srp1(packet, verbose=0, timeout=3)

try:
    print(response[ARP].hwsrc)
except:
    print("Error:+Timout.+Likely+IP+address+does+not+exist+on+LAN,+or+node+is+offline.")




