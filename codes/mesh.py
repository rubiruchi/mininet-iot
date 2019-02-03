#!/usr/bin/python

"""This example shows how to work in adhoc mode

It is a full mesh network

     .sta3.
    .      .
   .        .
sta1 ----- sta2"""

import sys

from mininet.log import setLogLevel, info
from mn_wifi.link import wmediumd, mesh
from mn_wifi.cli import CLI_wifi
from mn_wifi.net import Mininet_wifi
from mn_wifi.wmediumdConnector import interference


def topology(mobility):
    "Create a network."
    net = Mininet_wifi(link=wmediumd, wmediumd_mode=interference)

    info("*** Creating nodes\n")
    if mobility:
        sta1 = net.addStation('sta1')
        sta2 = net.addStation('sta2')
        sta3 = net.addStation('sta3')
    else:
        sta1 = net.addStation('sta1', position='10,10,0')
        sta2 = net.addStation('sta2', position='50,10,0')
        sta3 = net.addStation('sta3', wlans=2, position='90,10,0')
    rsu1 = net.addStation('rsu1', position='120,10,0')

    net.setPropagationModel(model="logDistance", exp=3.6)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Creating links\n")
    net.addLink(sta1, cls=mesh, ssid='meshNet',
                channel=5, ht_cap='HT40+', intf='sta1-wlan0') #, passwd='thisisreallysecret')
    net.addLink(sta2, cls=mesh, ssid='meshNet',
                channel=5, ht_cap='HT40+', intf='sta2-wlan0') #, passwd='thisisreallysecret')
    net.addLink(sta3, cls=mesh, ssid='meshNet',
                channel=5, ht_cap='HT40+', intf='sta3-wlan0') #, passwd='thisisreallysecret')
    rsu1.setMasterMode(intf='rsu1-wlan0', ssid='slice-ssid',
                       channel='11', mode='g')



    info("*** Starting network\n")
    net.build()

    sta3.cmd('ifconfig sta3-wlan1 192.168.0.3')

    info("*** Running CLI\n")
    CLI_wifi(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    mobility = True if '-m' in sys.argv else False
    topology(mobility)
