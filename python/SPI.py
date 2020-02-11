import wiringpi

CHANNEL = 0
SPEED = 500000

EMPTY_LIST = [0x00, 0x00, 0x00, 0x00]


class SPIhandler:
    def __init__(self):
        self.last_message = EMPTY_LIST[:]

        wiringpi.wiringPiSetupGpio()
        wiringpi.wiringPiSPISetup(CHANNEL, SPEED)

    def xfer(self, data):
        """data must be a quadruple of bytes in a list like so:
           [byte0, byte1, byte2, byte3]

           Returns a list with 9 elements containing a True or False
           for every button, and False if the input is the wrong
           amount of elements."""

        if len(data) is not 4:
            return False

        if data is not None:
            send = data[:]
        else:
            send = self.last_message[:]

        recv = wiringpi.wiringPiSPIDataRW(CHANNEL, bytes(send))[1]

        result = []

        for x in recv:
            for i in range(8):
                result.append((x >> i) & 1)

        self.last_message = send[:]

        return result[-9:]  # Only return the last 9 bits for the 9 buttons


spi = SPIhandler()

iinput = []
iinput.extend(input("INPUT:\n"))
iinput.extend(input("INPUT:\n"))
iinput.extend(input("INPUT:\n"))
iinput.extend(input("INPUT:\n"))
hinput = []
hinput.extend([int(iinput[0], 16)])
hinput.extend([int(iinput[1], 16)])
hinput.extend([int(iinput[2], 16)])
hinput.extend([int(iinput[3], 16)])

while True:
    print(spi.xfer(hinput))
