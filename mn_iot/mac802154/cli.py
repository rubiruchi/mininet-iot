import sys

from mn_iot.wifi.cli import CLI_wifi

class CLI_mac802154(CLI_wifi):
    "Simple command-line interface to talk to nodes."

    def __init__(self, mininet, stdin=sys.stdin, script=None):
        CLI_wifi.__init__(self, mininet, stdin=sys.stdin, script=None)

    def do_pingall(self, line):
        "Ping between all hosts."
        self.mn.pingAll(line)
