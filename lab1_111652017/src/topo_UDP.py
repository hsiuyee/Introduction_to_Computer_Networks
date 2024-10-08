from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.log import setLogLevel
import os

class MininetTopo(Topo):
    def build(self):
        # Add hosts to a topology
        self.addHost("h1")
        self.addHost("h2")
        self.addHost("h3")
        self.addHost("h4")
        
        # Add switchs to a topology
        self.addSwitch("s1")
        self.addSwitch("s2")
        self.addSwitch("s3")
        
        # Add bidirectional links to a topology, and set bandwidth(Mbps)
        self.addLink("h1", "s1", bw=2)
        self.addLink("h2", "s1", bw=2)
        self.addLink("s1", "s2", bw=2)
        self.addLink("s1", "s3", bw=2)
        self.addLink("s2", "h3", bw=2)
        self.addLink("s3", "h4", bw=2)
 
if __name__ == '__main__':
    setLogLevel('info')
    if not os.path.isdir("../out/"):
        os.mkdir("../out/")
        
    # Create a topology
    topo = MininetTopo() 
    
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo,
        controller = OVSController,
        link = TCLink)
    
    # Start a network
    net.start()
    
    
    ##### iperf #####
    h1, h2, h3, h4 = net.get("h1", "h2", "h3", "h4")
    
    h3.cmd('tcpdump -w ../out/UDP_h3.pcap &')
    h3.cmd('iperf -u -s -i 1 -t 5 -p 7787 > ../out/UDP_s_h3_1.txt &')
    h1.cmd('iperf -u -c ' + str(h3.IP()) + ' -i 1 -t 5 -p 7787 > ../out/UDP_c_h1_1.txt &')
    
    h3.cmd('iperf -u -s -i 1 -t 5 -p 7788 > ../out/UDP_s_h3_2.txt &')
    h1.cmd('iperf -u -c ' + str(h3.IP()) + ' -i 1 -t 5 -p 7788 > ../out/UDP_c_h1_2.txt &')
    
    h4.cmd('tcpdump -w ../out/UDP_h4.pcap &')
    h4.cmd('iperf -u -s -i 1 -t 5 -p 7789 > ../out/UDP_s_h4.txt &')
    h2.cmd('iperf -u -c ' + str(h4.IP()) + ' -i 1 -t 5 -p 7789 > ../out/UDP_c_h2.txt &')
    
    # open CLI
    CLI(net)
    net.stop()
''''
Traceback (most recent call last):
  File "topo_UDP.py", line 1, in <module>
    from mininet.net import Mininet
ModuleNotFoundError: No module named 'mininet'
'''
