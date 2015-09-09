###Instructions:  
You have to set some important system variables. To do that please run the following commands on terminal (maybe not necessary if you use `mininetCodeGenerator.py`):  

`ulimit -n 65000` (estimated value)    
`echo "kernel.pty.max = 50000" >> /etc/sysctl.conf` (estimated value)    
`sysctl -p`  

###Running the code:  
To run the code just type `python mininetPTT.py`, but you have to choose the PTT (IXP in Portuguese) before running it (assigning a name to 'filename' inside of mininetPTT.py file).  

####[Important]  
Depending of the PTT the process can take too long time (more than 1 or 2 hours) and require more than 160Gb of RAM memory. Alternatively you can use `mininetCodeGenerator.py` file and choose the number of ASes hops from the PTT that you want to remove. The file should create another one called `mininetCode.py` which you will use to generate the topology to Mininet.  

###Dependencies:   
Mininet - http://mininet.org  
Networkx - https://networkx.github.io   

###How Configure the Link among ASes  
The links among ASes are configured as follows:  

     if hops < 3:   
         bw=1000 
     else:   
         bw=100   
     delay=str(10+(hops*2))+'ms'  
**You may change the value for bw and delay if prefer (inside of `mininetCodeGenerator.py`).**  

####[File Size Details]  
[1] 126 bytes - Ptt_Path_SJC.txt  
[2] 27524 bytes - Ptt_Path_LDA.txt  
[3] 66240 bytes - Ptt_Path_SP.txt  
[4] 66312 bytes - Ptt_Path_PR.txt  
[5] 2338203 bytes - Ptt_Path_LAJ.txt  
[6] 2381375 bytes - Ptt_Path_MGF.txt   
[7] 2393014 bytes - Ptt_Path_SJP.txt   
[8] 2406054 bytes - Ptt_Path_DF.txt  
[9] 2449641 bytes - Ptt_Path_GYN.txt  
[10] 2463723 bytes - Ptt_Path_SCA.txt  
[11] 2596396 bytes - Ptt_Path_CXJ.txt  
[12] 3162836 bytes - Ptt_Path_MAO.txt  
[13] 4602615 bytes - Ptt_Path_BEL.txt   
[14] 4807284 bytes - Ptt_Path_PE.txt  
[15] 4888369 bytes - Ptt_Path_MG.txt    
[16] 4917649 bytes - Ptt_Path_RJ.txt   
[17] 5056202 bytes - Ptt_Path_SC.txt    
[18] 5309457 bytes - Ptt_Path_BA.txt    
[19] 5496507 bytes - Ptt_Path_CPV.txt   
[20] 5706345 bytes - Ptt_Path_AME.txt   
[21] 7098927 bytes - Ptt_Path_CE.txt   
[22] 7588089 bytes - Ptt_Path_NAT.txt    
[23] 7731698 bytes - Ptt_Path_CAS.txt   
[24] 8608186 bytes - Ptt_Path_CGB.txt   
[25] 10873057 bytes - Ptt_Path_VIX.txt   
[26] 59148359 bytes - Ptt_Path_RS.txt  

