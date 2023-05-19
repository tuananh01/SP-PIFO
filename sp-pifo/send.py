#!/usr/bin/env python3
import socket
import sys
from time import sleep
import os
import random
from scapy.all import *
from scapy.layers.inet import _IPOption_HDR


def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

###### 500-1000 Bytes packet ######
def rank_computation(pkt):
    rank = random.randint(399, 1001)
    if len(pkt) < rank:
        pad_len = rank - len(pkt)
        pad = Padding()
        pad.load = "/"*pad_len
        pkt = pkt / pad
    return pkt
###### 500-1000 Bytes packet ######


def main():
    if len(sys.argv)<2:
        print('pass 2 arguments: <destination> "<message>" <number of packets>')
        exit(1)
    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()
    payload = sys.argv[2]
    pkt_origin = Ether(src=get_if_hwaddr(iface), dst="ff:ff:ff:ff:ff:ff")/IP(dst=addr)/UDP(dport=4321, sport=1234)/payload

    #pkt_origin
 # tos=int(sys.argv[4])
 #   pkt = Ether(src=get_if_hwaddr(iface), dst="ff:ff:ff:ff:ff:ff") / IP(
 #       dst=addr, options = IPOption_MRI(count=2,
 #           swtraces=[SwitchTrace(swid=0,qdepth=0), SwitchTrace(swid=1,qdepth=0)])) / UDP(
 #           dport=4321, sport=1234) / sys.argv[2]


    pkt_origin.show2()
    total_pkts = 0
    try:
      for i in range(int(sys.argv[3])):
        pkt = rank_computation(pkt_origin)         #Assign packet sizes randomly from the origin packet
        sendp(pkt, iface=iface)                    #Send new calculated packet
        pkt = pkt_origin                           #Turn back into the original packet
        total_pkts += 1
        sleep(0)

      print("\nSent %s packets in total" % total_pkts)
    except KeyboardInterrupt:
        raise

if __name__ == '__main__':
    main()
