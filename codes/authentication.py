#!/usr/bin/python

'This example shows how to work with authentication'

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi


def topology():
    "Create a network."
    net = Mininet_wifi()

    info("*** Creating nodes\n")
    sta1 = net.addStation('sta1', passwd='123456789a', encrypt='wpa2', position='10,10,0')
    sta2 = net.addStation('sta2', passwd='123456789a', encrypt='wpa2', position='10,11,0')
    ap1 = net.addAccessPoint('ap1', ssid="simplewifi", mode="g", channel="1",
                             passwd='123456789a', encrypt='wpa2', position='10,13,0',
                             failMode="standalone", datapath='user')
    ap2 = net.addAccessPoint('ap2', ssid="simplewifi", mode="g", channel="1", position='10,15,0',
                             passwd='123456789a', encrypt='wpa2',
                             failMode="standalone", datapath='user')

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating Stations\n")
    net.addLink(sta1, ap1)
    net.addLink(sta2, ap1)

    info("*** Starting network\n")
    net.build()
    ap1.start([])
    ap2.start([])

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
