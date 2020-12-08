# CMPT 471 Group 16 - Router

![Alt text](/Diagram.png?raw=true "Network Topology")

## Steps:
```
cd ~/
git clone --branch rc-2.0.0 https://github.com/p4lang/p4app.git
```
#### Main Router

Launch Docker.
cd to the Repo Folder.
```
~/p4app/p4app run myrouter.p4app
```

#### Router with Bloom Counter

Launch Docker.
cd to the Repo Folder.
```
~/p4app/p4app run myrouterbloomcounter.p4app
```