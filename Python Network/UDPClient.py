#######################################################################################################
# A Python UDP client is not much different than a TCP client; we need to make only two small changes #
# to get it to send packets in UDP form.                                                              #   
#######################################################################################################

import socket
target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAABBBCCC",(target_host,target_port))

data, addr = client.recvfrom(4096)

print = data