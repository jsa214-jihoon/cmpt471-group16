# CMPT 471 Group 16 - Router

Topology Diagram:

<kbd>
<img src="Diagram.png" alt="Network Topology" width="400" style="border-radius:50%" />
</kbd>

## Steps:

#### Installing Requirements
Install *p4app* with the following commands. *p4app* allows building, running, debugging, and testing P4 programs.
```
cd ~/
git clone --branch rc-2.0.0 https://github.com/p4lang/p4app.git
```
Clone this project's repository into desired location.
```
git clone https://github.com/jsa214-jihoon/cmpt471-group16.git
```
#### Main Router
Launch Docker.
On Docker Terminal, cd to the repository folder containing *myrouter.p4app* folder and run the following command.
```
~/p4app/p4app run myrouter.p4app
```
Possible commands include pinging one host from another,
```
h1 ping h2
```
.

According to the topology, there is a firewall at S2 where h2/h3 can reach h1/h4/h5, but not the other way around. Exception is given for h5, so that h5 can still reach h2 and h3.

For example:
```
iperf h2 h1
```
-> works.
```
iperf h1 h2
```
-> does not work.
```
iperf h5 h3
```
-> works.
#### Router with Bloom Counter

Launch Docker.
On Docker Terminal, cd to the repository folder containing *myrouterbloomcounter.p4app* folder and run the following command.
```
~/p4app/p4app run myrouterbloomcounter.p4app
```
