# SP-PIFO
This repository provides the code of SP-PIFO and my implementation of SP-PIFO on BMv2.
## Original work
Authors' github: https://github.com/nsg-ethz/SP-PIFO/tree/master
<br>
Official document of SP-PIFO: https://www.usenix.org/conference/nsdi20/presentation/alcoz
## My implementation
About the simulation environment, I use the latest Development VM which has necessary P4 developement tools provided here: https://github.com/jafingerhut/p4-guide/blob/master/bin/README-install-troubleshooting.md
<br>
I clone p4-learning repository (https://github.com/nsg-ethz/p4-learning/tree/master) to the VM and using that repo to run exercises.
<br>
<br>
The sp-pifo folder in this repository include:
<li> <b>sp-pifo.p4</b>: p4_16 code of SP-PIFO </li>
<li> <b>network.py</b>: Used to create network topology
<li> <b>send.py</b>:    Python code using Scapy library used to create and send packets </li>
<li> <b>receive.py</b>: Python code using Scapy library used to receive packets </li>
<li> <b>sw_commands folder</b>: Contain .txt files used to configure forwarding rules for switches </li>
</br>
<hr>
<b> Topology </b>
<p>
    <img src="https://github.com/tuananh01/SP-PIFO/assets/86756286/4fafe01f-0e2c-486f-b965-5ce5ff53c84d/topology.svg"/>
</p>
To run the code, go to the terminal and enter the command: <code>sudo python3 network.py</code>
<br>
This will compile the p4 code and also generate the topology in Mininet: 
<p>
    <img src="https://github.com/tuananh01/SP-PIFO/assets/86756286/700337c5-a39f-4bbe-867f-9eceb82fc484">
</p>
<br>
SP-PIFO uses ranking mechanism to select priority queue for each packet. According to the authors, the rank can be computed in the switch or in the end-host and read it from the switch. The current code in the authors' github is for the case in which you compute the rank at the end host, tag it into the ToS field of IP packets, and read it for the switch. 
<br>
<br>
In my case, I write a function in <code> send.py </code> to randomly set the packet size for each packet before sending it and use the packet size for ranking mechanism where smaller sizes have higher priority. In addition, I tag the <code> standard_metatata.qid </code> to ToS fields of IP packets to distinguish different priority queues.
<br> 
Sending packets between two hosts using <code> xterm </code> commands in Mininet.
<br>
<br>
For example, I send 10 packets from h1 to h3:
<p>
    <img src="https://github.com/tuananh01/SP-PIFO/assets/86756286/34d57759-7033-43cf-819e-423afe38e11d">
</p>
The result of the ranking mechanism can be checked by using CLI of simple_switch to read the register used to capture queue bound values:
<p>
    <img src="https://github.com/tuananh01/SP-PIFO/assets/86756286/d3714e5a-6865-4ba2-8661-e80de02ab01f">
</p>
Or using .log files in the log folder generated after compiling the code
<p>
    <img src="https://github.com/tuananh01/SP-PIFO/assets/86756286/a2fad31e-235e-4c71-900e-b01be577f095f">
</p>
<br>
If you want to delete log and pcap folder, hit <code> Ctrl+D </code> to exit Mininet and enter the command:
<br>
<code> sudo make clean </code>
