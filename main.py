from machine import UART, Pin

uart = UART(16, baudrate=9600)
HC05 = Pin(14, Pin.OUT)
HC05.value(1) #Leave bluetooth on
ESC = Pin(34, Pin.OUT)

while True:
    if uart.any():
        data_received = str(uart.readline())
        if 'Throttle On' in data_received:
            ESC.on()
    else:
        ESC.off()
     
    
    
    
