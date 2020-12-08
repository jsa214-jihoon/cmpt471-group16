# CMPT 471 Group 16 - Router

Topology Diagram:
<kbd>
<img src="Diagram.png" alt="Network Topology" width="400" style="border-radius:50%" />
</kbd>

## Steps:
Clone the p4app that is used for the Project.
```
cd ~/
git clone --branch rc-2.0.0 https://github.com/p4lang/p4app.git
```
#### Main Router

Launch Docker.
Then, cd to the Repo Folder.
```
~/p4app/p4app run myrouter.p4app
```

#### Router with Bloom Counter

Launch Docker.
Then, cd to the Repo Folder.
```
~/p4app/p4app run myrouterbloomcounter.p4app
```
