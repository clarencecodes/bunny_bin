import time
from gpiozero import MCP3008
 
divider = MCP3008(0)

while True:
    print(divider.value)
    print(str(28250/(divider.value-229.5))+"centimeters")
    time.sleep(1)
