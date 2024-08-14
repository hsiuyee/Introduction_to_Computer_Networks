/*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include "ns3/applications-module.h"
#include "ns3/core-module.h"
#include "ns3/internet-module.h"
#include "ns3/network-module.h"
#include "ns3/point-to-point-module.h"

// Default Network Topology
//
//       10.1.1.0
// n0 -------------- n1
//    point-to-point
//

using namespace ns3;

NS_LOG_COMPONENT_DEFINE("FirstScriptExample");

int
main(int argc, char* argv[])
{
    CommandLine cmd(__FILE__);
    cmd.Parse(argc, argv);

    Time::SetResolution(Time::NS);
    LogComponentEnable("UdpEchoClientApplication", LOG_LEVEL_INFO);
    LogComponentEnable("UdpEchoServerApplication", LOG_LEVEL_INFO);

    NodeContainer nodes;
    nodes.Create(3);

    PointToPointHelper pointToPoint1; 
    pointToPoint1.SetDeviceAttribute("DataRate", StringValue("2Mbps"));
    pointToPoint1.SetChannelAttribute("Delay", StringValue("2ms"));
    NetDeviceContainer devices1 = pointToPoint1.Install(nodes.Get(0), nodes.Get(1)); // flow 1

    PointToPointHelper pointToPoint3; 
    pointToPoint3.SetDeviceAttribute("DataRate", StringValue("3Mbps"));
    pointToPoint3.SetChannelAttribute("Delay", StringValue("2ms"));
    NetDeviceContainer devices3 = pointToPoint3.Install(nodes.Get(0), nodes.Get(2)); // flow 3

    InternetStackHelper stack;
    stack.Install(nodes);

    Ipv4AddressHelper address1;
    address1.SetBase("10.0.1.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces1 = address1.Assign(devices1);

    Ipv4AddressHelper address2;
    address2.SetBase("10.0.2.0", "255.255.255.0");
    Ipv4InterfaceContainer interfaces2 = address2.Assign(devices3);

    UdpEchoServerHelper echoServer1(99);

    ApplicationContainer serverApps1 = echoServer1.Install(nodes.Get(1));
    serverApps1.Start(Seconds(1.0));
    serverApps1.Stop(Seconds(10.0));
    UdpEchoClientHelper echoClient1(interfaces1.GetAddress(1), 99);
    echoClient1.SetAttribute("MaxPackets", UintegerValue(4));
    echoClient1.SetAttribute("Interval", TimeValue(Seconds(1.0)));
    echoClient1.SetAttribute("PacketSize", UintegerValue(1024));
    ApplicationContainer clientApps1 = echoClient1.Install(nodes.Get(0));
    clientApps1.Start(Seconds(2.0));
    clientApps1.Stop(Seconds(10.0));


    UdpEchoServerHelper echoServer2(98);
    ApplicationContainer serverApps2 = echoServer2.Install(nodes.Get(2));
    serverApps2.Start(Seconds(1.0));
    serverApps2.Stop(Seconds(10.0));
    UdpEchoClientHelper echoClient2(interfaces2.GetAddress(1), 98);
    echoClient2.SetAttribute("MaxPackets", UintegerValue(4));
    echoClient2.SetAttribute("Interval", TimeValue(Seconds(1.0)));
    echoClient2.SetAttribute("PacketSize", UintegerValue(1024));
    ApplicationContainer clientApps2 = echoClient2.Install(nodes.Get(0));
    clientApps2.Start(Seconds(2.0));
    clientApps2.Stop(Seconds(10.0));

    Simulator::Run();
    Simulator::Destroy();
    return 0;
}