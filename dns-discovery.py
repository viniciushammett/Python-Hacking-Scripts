import socket

domain = "write the domain.com here"

with open("brute-force.txt") as file:
    name = file.readlines()

for name in name:
    DNS = name.strip("\n") + "." + domain
    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass
