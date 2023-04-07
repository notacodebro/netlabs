import cli
""" this module is located directly in the c9k site-packages as this script should 
be run directly in the guest shell or the ztp bootstrap process"""

print "\n\n *** Executing show version *** \n\n"
cli.executep('show version')
""" note this code is written for 2.x and will operate with the included interperter"""

print "\n\n *** Configuring a Loopback Interface *** \n\n"
cli.configurep(["interface loop 100", "ip address 10.10.10.10 255.255.255.255", "end"])
cli.configurep(["hostname ConfiguredWithZTP", "end"])

print "\n\n *** Executing show ip interface brief *** \n\n"
cli.executep('show ip int brief')

print "\n\n *** ZTP/Guest-shell python script complete *** \n\n"
