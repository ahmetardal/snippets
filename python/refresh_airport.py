#
#  refresh_airport.py
#
#  Created by Ahmet Ardal on 2/3/11.
#

import re
import os
import time

def refreshAirport():
    """
    switches airport off and on on MacOSX to solve temporary wireless connectivity problems
    """
    
    # get network interfaces list
    pipe = os.popen("networksetup -listallhardwareports", "r")
    networkInterfaces = pipe.read().strip()
    
    # parse and get exact AirPort interface name
    regexp = re.compile("AirPort\nDevice: [a-z]+[0-9]*", re.IGNORECASE)
    match = regexp.findall(networkInterfaces)
    airportLine = match[0]
    airportIFName = airportLine.partition(": ")[2]
    
    # switch it off and turn it on after some delay
    airportPowerCtlCmd = "networksetup -setairportpower " + airportIFName
    os.system(airportPowerCtlCmd + " off")
    time.sleep(3)
    os.system(airportPowerCtlCmd + " on")

def main():
    refreshAirport()
    print "OK, Done."
    
if __name__ == "__main__":
    main()
