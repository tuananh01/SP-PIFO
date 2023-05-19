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
<li> sp-pifo.p4: p4_16 code of SP-PIFO
<li> network.py: Used to create network topology
<li> send.py: Python code using Scapy library used to create and send packets 
<li> receive.py: Python code using Scapy library used to receive packets
<li> sw_commands folder: Contain .txt files used to configure forwarding rules for switches
<br>
<hr>
The topology
<br>
