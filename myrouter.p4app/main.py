from p4app import P4Mininet

from mytopo import CustomTopo

topo = CustomTopo()
net = P4Mininet(program="router.p4", topo=topo)
net.start()

h1, h2, h3, h4, h5 = net.get("h1"), net.get("h2"), net.get("h3"), net.get("h4"), net.get("h5")
s1, s2, s3, s4 = net.get("s1"), net.get("s2"), net.get("s3"), net.get("s4")

def addForwardingRule(sw, host, port):
    sw.insertTableEntry(table_name="MyIngress.ipv4_lpm",
                        match_fields={'hdr.ipv4.dstAddr': ["10.0.0.%d" % host, 32]},
                        action_name="MyIngress.ipv4_forward",
                        action_params={'dstAddr': "00:00:00:00:00:0%d" % host,
                                       'port': port}
                        )

def addFirewallRule(sw, inPort, outPort, direction):
    sw.insertTableEntry(table_name ="MyIngress.check_ports",
                        match_fields = { "standard_metadata.ingress_port": inPort, 
                                        "standard_metadata.egress_spec": outPort},
                        action_name = "MyIngress.set_direction",
                        action_params = {"dir": direction}
                        )

#current topology
#               (h1)
#                 |
#                 |
#                 1
#               (s1)
#              2    3
#             /      \  
#            /        \
#           2          2 
#         (s2) 3 --- 3 (s3)
#        1    4            1
#       /      \            \
#      /        \            \
#    (h2)      (h3)         (h4)

# Set Forwarding for S1
for host, port in [(1,1), (2,2), (3,2), (4,3), (5, 3)]:
    addForwardingRule(s1, host, port)

# Set Forwarding for S2
for host, port in [(1,2), (2,1), (3,4), (4,3), (5,3)]:
    addForwardingRule(s2, host, port)

# Set Forwarding for S3
for host, port in [(1,2), (2,3), (3,3), (4,1), (5,2)]:
    addForwardingRule(s3, host, port)

# Set Forwarding for S4
for host, port in [(1,2), (2,3), (3,3), (4,3), (5,1)]:
    addForwardingRule(s4, host, port)
    
# Firewall Rules for S2
for inPort, outPort in [(1,2), (2,1), (2,4), (4,2), (3,4), (4,3), (1,3), (3,1)]:
    if inPort == 2 or inPort == 3:
        direction = 1
    else:
        direction = 0
    
    addFirewallRule(s2, inPort, outPort, direction)

# Allow h5 to contact h2 and h3 even though it comes from port 3
s2.insertTableEntry(table_name="MyIngress.allowed_hosts",
                    match_fields={'hdr.ipv4.srcAddr': "10.0.0.5"},
                    action_name = "NoAction",
                    action_params = {}
                    )

loss = net.pingAll()
assert loss == 0

# Start the mininet CLI to interactively run commands in the network:
from mininet.cli import CLI
CLI(net)

# JIHOON #
print('\n')
print('Traffic Stats: \n')
print('s1 IP packet counter: ' + str(s1.readCounter('ip_packets', 1)[0]))
# print('S1 ARP packets: ' + str(s1.readCounter('switch_arp_packets', 1)[0]))
print('s2 IP packet counter: ' + str(s2.readCounter('ip_packets', 1)[0]))
# print('S2 ARP packets: ' + str(s2.readCounter('switch_arp_packets', 1)[0]))
print('s3 IP packet counter: ' + str(s3.readCounter('ip_packets', 1)[0]))
# print('S3 ARP packets: ' + str(s3.readCounter('switch_arp_packets', 1)[0]))
