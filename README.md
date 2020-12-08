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