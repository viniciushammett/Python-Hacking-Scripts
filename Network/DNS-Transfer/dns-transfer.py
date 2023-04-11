import dns.query
import dns.zone
import dns.resolver

domain = "Write the domain here"
registerNS = dns.resolver.query(domain, "NS")
lista = []

for register in registerNS:
    lista.append( str(register) )

for registro in lista:
    try:
        ZoneTransfer = dns.zone.from_xfr(dns.query.xfr(register, domain))
    except:
        print("Error")
    else: 
        registerDNS = list(ZoneTransfer.nodes.keys())
        registerDNS.sort()
        for n in registerDNS:
            print(ZoneTransfer[n].to_text(n))