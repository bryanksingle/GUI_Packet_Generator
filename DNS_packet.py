from scapy.all import *
import whois

#DNS packet handler

def check_reg(name):
        domain_info = whois.whois(name)
        if domain_info.status:
            return True
        return False

dname = str(sys.argv[1])
ipV = int(sys.argv[2])
toggle = sys.argv[3]

################Error Checking###################

test = check_reg(dname)
if (test==False):
    print("Error: Domain Name Not Found")
    sys.exit()

match int(ipV):
    case 4:
        ip = IP(dst="1.1.1.1")
        dns = DNS(rd=1, qd=DNSQR(qname=dname))
    case 6:
        ip = IPv6(dst="2001:4860:4860::8888")
        dns = DNS(rd=1, qd=DNSQR(qname=dname, qtype = "AAAA"))
    case _:
        print("Error: Unknown IP Version, Try 4 or 6")
        sys.exit()

#################################################

packet = ip / UDP() / dns
if (toggle=='False'):
        response = send(packet)
        sys.exit()
        
response = sr1(packet, verbose =0)

for x in range(response[DNS].ancount):
    
    if isinstance(response[DNSRR][x].rdata, (bytes,bytearray)):
        continue
    print(response[DNSRR][x].rdata)





