###Instructions:  

You have to set up some important system variables. To do that please run the following commands:  

`ulimit -n 65000` (estimated value)    
`echo "kernel.pty.max = 50000" >> /etc/sysctl.conf` (estimated value)    
`sysctl -p`  

###Running the code:  

To run the code just type `python mininetPTT.py`, but you have to choose the PTT (IXP in Portuguese) before running it (assigning a name to 'filename' inside of the mininetPTT.py file).  

####[Important]  
Depending of the code the process can take too long time (more than 1 hour) and require more than 32Gb of RAM memory.  

####[File Details]  
126 Ptt_Path_SJC.txt  
27524 Ptt_Path_LDA.txt  
66240 Ptt_Path_SP.txt  
66312 Ptt_Path_PR.txt  
2338203 Ptt_Path_LAJ.txt  
2381375 Ptt_Path_MGF.txt   
2393014 Ptt_Path_SJP.txt   
2406054 Ptt_Path_DF.txt  
2449641 Ptt_Path_GYN.txt  
2463723 Ptt_Path_SCA.txt  
2596396 Ptt_Path_CXJ.txt  
3162836 Ptt_Path_MAO.txt  
4602615 Ptt_Path_BEL.txt   
4807284 Ptt_Path_PE.txt  
4888369 Ptt_Path_MG.txt    
4917649 Ptt_Path_RJ.txt   
5056202 Ptt_Path_SC.txt    
5309457 Ptt_Path_BA.txt    
5496507 Ptt_Path_CPV.txt   
5706345 Ptt_Path_AME.txt   
7098927 Ptt_Path_CE.txt   
7588089 Ptt_Path_NAT.txt    
7731698 Ptt_Path_CAS.txt   
8608186 Ptt_Path_CGB.txt   
10873057 Ptt_Path_VIX.txt   
59148359 Ptt_Path_RS.txt  

