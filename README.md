# CMPT 471 Group 16 - Router

Topology Diagram:

<kbd>
<img src="Diagram.png" alt="Network Topology" width="400" style="border-radius:50%" />
</kbd>

## Steps:

#### Install Requirements
Install *p4app* with the following commands. *p4app* allows building, running, debugging, and testing P4 programs.
```
cd ~/
git clone --branch rc-2.0.0 https://github.com/p4lang/p4app.git
```
Clone this project's repository into a desired location.
```
git clone https://github.com/jsa214-jihoon/cmpt471-group16.git
```
#### Main Router
Launch Docker.
On the Docker Terminal, *cd* to the repository folder containing the *myrouter.p4app* folder and run the following command.
```
~/p4app/p4app run myrouter.p4app
```
To test the program, different commands are available such as:
```
<src hostname> ping <dst hostname>
iperf <src hostname> <dst hostname>
```


According to the topology, there is a firewall at s2 where h2/h3 can reach h1/h4/h5, but not the other way around. Exception is given for h5, where h5 can still reach h2 and h3.

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
On the Docker Terminal, *cd* to the repository folder containing the *myrouterbloomcounter.p4app* folder and run the following command.
```
~/p4app/p4app run myrouterbloomcounter.p4app
```
