#!/usr/bin/python

"""
Mininet Code to run PTT (Pontos de troca de trafego do Brasil) or Brazilian IXP (Internet Exchange Points)
author: Ramon Fontes - ramonrf@dca.fee.unicamp.br
                       ramonreisfontes@gmail.com
"""

import networkx as nx
import os

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

outputFileName = 'mininetCode.py'

def topology():
    
    if(os.path.exists('mininetCode.py')):
        os.system('rm mininetCode.py')
    
    os.system('echo "from mininet.net import Mininet" >> %s' % outputFileName)
    os.system('echo "from mininet.node import Controller, OVSKernelSwitch" >> %s' % outputFileName)
    os.system('echo "from mininet.cli import CLI" >> %s' % outputFileName)
    os.system('echo "from mininet.log import setLogLevel" >> %s' % outputFileName)
    os.system('echo "from mininet.link import TCLink" >> %s' % outputFileName)
    
    os.system('echo "\ndef topology():" >> %s' % outputFileName)
    
    removeNodes = []
    hashost = []
   
    filename = raw_input('Please enter the filename: ')

    "Create a network."
    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )
    os.system('echo "\n    net = Mininet( controller=Controller, link=TCLink, switch=OVSKernelSwitch )" >> %s\n\n' % (outputFileName))
    
    excludedLine = 0
    i=0;k=1;j=0
    node = [[0 for x in xrange(50)] for x in xrange(333300)]
    e1=open(str(filename), 'r') # read info file
    A=nx.Graph()

    for line in e1:
        count=len(line.strip().split(' '))
        if (line.strip().split(' ')[count-1]==str(26121) or line.strip().split(' ')[count-1]==str(20121)):
            excludedLine+=1
        else:
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
            
    Degree = int(raw_input('Please enter the number of degree which you want to remove: '))
    
    for x in A.nodes():
        if len(nx.shortest_path(A,source=26121,target=x)) > Degree:
            removeNodes.append(x)
    
    hosts = raw_input('Please enter the ASN to add host (you can type for multiple: 100,101,102): ')
    hosts = hosts.split(',')
    
    A.remove_nodes_from(removeNodes)
    print "*** Creating %s nodes"%len(A.nodes())
    asn=[0 for x in xrange(len(A.nodes()))]
    x=0
    os.system('echo "\n    print \'*** Creating %s nodes ***\'" >> %s' % (len(A.nodes()), outputFileName))
    
    for switch in A.nodes():
        asn[x] = net.addSwitch( 'ASN%s' % switch )
        os.system('echo "    ASN%s = net.addSwitch( \'ASN%s\' )" >> %s' % (switch, switch, outputFileName)) 
        x+=1
    
    for host in hosts:
        for node in A.nodes():
            if str(host) == str(node):
                net.addHost('h%s' % str(host))
                print "net.addHost( 'h%s' )" % str(host)
                os.system('echo "    h%s = net.addHost( \'h%s\' )" >> %s' % (str(host), str(host), outputFileName)) 
                A.add_edge(str(node), str(host))    
    
    c1 = net.addController( 'c1' )
    os.system('echo "\n    c1 = net.addController( \'c1\' )" >> %s' % (outputFileName))

    print "*** Creating links ***"
    os.system('echo "\n    print \'*** Creating Links ***\'" >> %s' % (outputFileName))
    i=0;k=1;j=0
    node = [[0 for x in xrange(50)] for x in xrange(333300)]
    e2=open(str(filename), 'r') # read info file
    for line in e2:
        count=len(line.strip().split(' '))
        if (line.strip().split(' ')[count-1]==str(26121) or line.strip().split(' ')[count-1]==str(20121)):
            print str(excludedLine) + "paths was removed!"
        else:
            while i <= count:
                if (i==0):
                    node[j][i]=26121
                elif((i>0) and (node[j][k-1]!=int(line.strip().split(' ')[i-1]))):
                    node[j][k] = int(line.strip().split(' ')[i-1])
                    if node[j][k] in A.nodes() and node[j][k-1] in A.nodes():
                        distance = len(nx.shortest_path(A,source=26121,target=node[j][k-1]))-1
                        if distance < 3:
                            bw=1000
                        else:
                            bw=100
                        delay=str(10+(distance*2))+'ms'
                        
                        if str(node[j][k]) in hosts and node[j][k] not in hashost:
                            print net.addLink("ASN%s"%node[j][k],'h%s'%node[j][k])
                            print net.addLink("ASN%s"%node[j][k-1],"ASN%s"%node[j][k], bw=bw, delay=delay)
                            os.system('echo "    net.addLink(\'ASN%s\',\'h%s\')" >> %s' % (node[j][k], node[j][k], outputFileName)) 
                            os.system('echo "    net.addLink(\'ASN%s\',\'ASN%s\', bw=%s, delay=\'%s\')" >> %s' % (node[j][k-1], node[j][k], bw, delay, outputFileName)) 
                            hashost.append(node[j][k])
                        elif str(node[j][k-1]) in hosts and node[j][k-1] not in hashost:
                            print net.addLink('h%s'%node[j][k],"ASN%s"%node[j][k])
                            print net.addLink("ASN%s"%node[j][k-1],"ASN%s"%node[j][k], bw=bw, delay=delay)
                            os.system('echo "    net.addLink(\'h%s\',\'ASN%s\'%)" >> %s' % (node[j][k], node[j][k], outputFileName)) 
                            os.system('echo "    net.addLink(\'ASN%s\',\'ASN%s\', bw=%s, delay=\'%s\')" >> %s' % (node[j][k-1], node[j][k], bw, delay, outputFileName)) 
                            hashost.append(node[j][k-1])
                        if str(node[j][k]) not in hosts and str(node[j][k-1]) not in hosts:
                            print net.addLink("ASN%s"%node[j][k-1],"ASN%s"%node[j][k], bw=bw, delay=delay)
                            os.system('echo "    net.addLink(\'ASN%s\',\'ASN%s\', bw=%s, delay=\'%s\')" >> %s' % (node[j][k-1], node[j][k], bw, delay, outputFileName)) 
                        k+=1
                i+=1
            i=0
            k=1
            j+=1

    print "*** Starting network ***"
    os.system('echo "\n    print \'*** Starting network ***\'" >> %s' % (outputFileName)) 
    
    net.build()
    c1.start()
    os.system('echo "    net.build()" >> %s' % (outputFileName)) 
    os.system('echo "    c1.start()\n" >> %s' % (outputFileName)) 
    
    x=0
    for nodes in A.nodes():
        if nodes not in hosts:
            asn[x].start( [c1] )
            os.system('echo "    %s.start( [c1] )" >> %s' % (asn[x], outputFileName)) 
            x+=1

    print "*** Running CLI"
    CLI( net )
    os.system('echo "\n    print \'*** Running CLI ***\'" >> %s' % (outputFileName)) 
    os.system('echo "    CLI( net )" >> %s' % (outputFileName)) 
   

    print "*** Stopping network"
    net.stop()
    os.system('echo "\n    print \'*** Stopping network ***\'" >> %s' % (outputFileName)) 
    os.system('echo "    net.stop()" >> %s' % (outputFileName)) 
   

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()
    
    os.system('echo "\nif __name__ == \'__main__\':" >> %s' % (outputFileName)) 
    os.system('echo "    setLogLevel( \'info\' )" >> %s' % (outputFileName)) 
    os.system('echo "    topology()" >> %s' % (outputFileName)) 

