import time
from gpiozero import MCP3008
 
divider = MCP3008(0)

while True:
    print(divider.value)
    # print(str(28250/(divider.value-229.5))+"centimeters")
    inches = 6202.3*divider.value^-1.056
    print(str(inches))
    time.sleep(1)
