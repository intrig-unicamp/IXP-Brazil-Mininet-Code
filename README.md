###Instructions:  

You have to set up some important system variables. To do that please run the following commands:  

`ulimit -n 65000` (estimated value)    
`echo "kernel.pty.max = 50000" >> /etc/sysctl.conf` (estimated value)    
`sysctl -p`  

###Running the code:  

To run the code just type `python mininetPTT.py`, but you have to choose the PTT (IXP in Portuguese) before running it (assigning a name to 'filename' inside of the mininetPTT.py file).  

####[Important]  
Depending of the code the process can take too long time (more than 1 hour) and require more than 32Gb of RAM memory.  
