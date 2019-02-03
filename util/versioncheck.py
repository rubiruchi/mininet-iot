#!/usr/bin/python

from subprocess import check_output as co
from sys import exit

# Actually run bin/mn rather than importing via python path
version = 'Mininet-IoT ' + co( 'PYTHONPATH=. bin/mn --iot --version 2>&1', shell=True )
version = version.strip()

# Find all Mininet-WiFi path references
lines = co( "egrep -or 'Mininet-IoT [0-9\.\+]+\w*' *", shell=True )

error = False

for line in lines.split( '\n' ):
    if line and 'Binary' not in line:
        fname, fversion = line.split( ':' )
        if version != fversion:
            print( "%s: incorrect version '%s' (should be '%s')" % (
                fname, fversion, version ) )
            error = True

if error:
    exit( 1 )
