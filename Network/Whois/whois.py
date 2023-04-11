import sys
try:
    import whois
except:
    sys.exit("[!] Install the nmap library using the command: pip3 install python-whois")

domain = "Type the domain right here"
Whoisinfo = whois.whois(domain)

print(Whoisinfo.email)
print(Whoisinfo["email"])
print(Whoisinfo.text)