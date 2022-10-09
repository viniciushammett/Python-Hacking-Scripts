###########################################################################################################
# There have been countless times during penetration tests that I’ve needed to whip up a TCP client to    #
# test for services, send garbage data, fuzz, or any number of other tasks. If you are working within the #
# confines of large enterprise environments, you won’t have the luxury of networking tools or             #  
# compilers, and sometimes you’ll even be missing the absolute basics like the ability to copy/paste or   # 
# an Internet connection. This is where being able to quickly create a TCP client comes in extremely      #
# handy. But enough jabbering — let’s get coding. Here is a simple TCP client                             # 
###########################################################################################################

import socket

target_host = "www.google.com"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)