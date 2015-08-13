#!/usr/bin/python

"""
Mininet Code to run PTT (Pontos de troga de trafego no Mininet) or IXP (Internet Exchange Points)
author: Ramon Fontes - ramonrf@dca.fee.unicamp.br
                       ramonreisfontes@gmail.com
"""

import networkx as nx
import os

from mininet.net import Mininet
from mininet.node import RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink


def topology():
    
    #PTT name
    filename='Ptt_Path_SJC.txt'

    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

    i=0;k=1;j=0
    node = [[0 for x in xrange(50)] for x in xrange(333300)]
    e1=open(str(filename), 'r') # read info file
    A=nx.Graph()

    for line in e1:
        count=len(line.strip().split(' '))
        while i <= count:
            if (i==0):
                node[j][i]=26121
            elif((i>0) and (node[j][k-1]!=int(line.strip().split(' ')[i-1]))):
                node[j][k] = int(line.strip().split(' ')[i-1])
                A.add_edge(node[j][k-1],node[j][k])
	        k+=1
            i+=1
        i=0
        k=1
        j+=1

    print "*** Creating %s nodes"%len(A.nodes())
    asn=[0 for x in xrange(len(A.nodes()))]
    x=0

    for nodes in A.nodes():
        asn[x] = net.addSwitch( 'ASN%s' % nodes )
        x+=1

    #h2 = net.addHost( 'h2', mac='00:00:00:00:00:02', ip='10.0.0.2/8' )
    c3 = net.addController( 'c3', ip='127.0.0.1', port=6633 )

    print "*** Creating links"
    i=0;k=1;j=0
    node = [[0 for x in xrange(50)] for x in xrange(333300)]
    e2=open(str(filename), 'r') # read info file

    for line in e2:
        count=len(line.strip().split(' '))
        while i <= count:
            if (i==0):
                node[j][i]=26121
            elif((i>0) and (node[j][k-1]!=int(line.strip().split(' ')[i-1]))):
                node[j][k] = int(line.strip().split(' ')[i-1])
                print net.addLink("ASN%s"%node[j][k-1],"ASN%s"%node[j][k])
                k+=1
            i+=1
        i=0
        k=1
        j+=1

    print "*** Starting network"
    net.build()
    c3.start()

    x=0
    for nodes in A.nodes():
        asn[x].start( [c3] )
        x+=1

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

