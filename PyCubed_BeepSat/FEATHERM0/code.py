import board
import busio
import digitalio
import pycubed_rfm9x
import time


'''
NOTE! this board doesn't have very much memory (both flash & RAM)

1.Once you have this board listening (and it's terminal open)...
2.on pycubed board in REPL
    from pycubed import cubesat
    cubesat.radio2.send('hi')
'''


CS = digitalio.DigitalInOut(board.RFM9X_CS)
RESET = digitalio.DigitalInOut(board.RFM9X_RST)

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# Initialze RFM radio
rfm9x = pycubed_rfm9x.RFM9x(spi=spi, cs=CS, reset=RESET, frequency=433.0, code_rate=8,baudrate=1320000)
rfm9x.enable_crc=True

count=0
while True:


    print("Sending message.....")
    #rfm9x.send(b"Hello... " + str(count))
    if count==15:
        print("Sending Killswitch")
        rfm9x.send(b"killswitch")
    else:
        rfm9x.send(b"Hello... " + str(count))
    send_time=time.monotonic()
    print(send_time)
    packet_rec = rfm9x.receive(timeout=2.0) # blocking listen for 2 seconds
    rec_time=time.monotonic()
    print(rec_time)
    if packet_rec is None:
        print("Received nothing! Listening again...")
        count=0
    else:
        print("Received (raw bytes): {0}".format(packet_rec))
        packet_text = str(packet_rec, "ascii")
        print("Received (ASCII): {0}".format(packet_text))
        rssi = rfm9x.last_rssi
        print("Received signal strength: {0} dB".format(rssi))
        count=count+1


