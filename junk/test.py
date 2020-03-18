import time
from gpiozero import MCP3008
 
divider = MCP3008(0)

while True:
    print(divider.value)
    v=(divider.value/1023.0)*3.3
    dist = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 301.439
    print "Distanz: %.2f cm" % dist
    time.sleep(1)
