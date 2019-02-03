#!/usr/bin/env python

"Setuptools params"

from setuptools import setup
from os.path import join

# Get version number from source tree
import sys
sys.path.append( '.' )
from mn_wifi.net import VERSION

scripts = [ join( 'bin', filename ) for filename in [ 'mn' ] ]

modname = distname = 'mininet-iot'

setup(
    name=distname,
    version=VERSION,
    description='Process-based OpenFlow emulator',
    author='Bob Lantz; Ramon Fontes',
    author_email='rlantz@cs.stanford.edu; ramonrf@dca.fee.unicamp.br',
    packages=[ 'mn_iot', 'mn_iot.wifi', 'mn_iot.mac802154', 'mn_iot.wmediumd.data',
               'mn_iot.examples', 'mn_iot.sumo', 'mn_iot.sumo.sumolib',
               'mn_iot.sumo.traci', 'mn_iot.sumo.data', 'mn_iot.sumo.sumolib.net',
               'mn_iot.sumo.sumolib.output', 'mn_iot.sumo.sumolib.shapes' ],
    package_data={'mn_iot.sumo.data': ['*.xml', '*.sumocfg'], 'mn_iot.wmediumd.data': ['signal_table_ieee80211ax',
                                                                                'signal_table_ieee80211n_gi20',
                                                                                'signal_table_ieee80211n_gi40',
                                                                                'signal_table_ieee80211n_sgi20',
                                                                                'signal_table_ieee80211n_sgi40']},
    long_description="""
        Mininet-WiFi is a network emulator which uses lightweight
        virtualization to create virtual networks for rapid
        prototyping of Software-Defined Wireless Network (SDWN) designs
        using OpenFlow.
        """,
    classifiers=[
          "License :: OSI Approved :: BSD License",
          "Programming Language :: Python",
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Topic :: System :: Emulators",
    ],
    keywords='networking emulator protocol Internet OpenFlow SDN',
    license='BSD',
    install_requires=[
        'setuptools'
    ],
    scripts=scripts,
)
