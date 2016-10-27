import serial

class LCDControl():
    def __init__(self):
        self._s = serial.Serial('/dev/ttyACM0', 9600)

    def clear(self):
        self.reset_cursor()
        self._s.write(b'\xFE\x51')

    def reset_cursor(self):
        self._s.write(b'\xFE\x45\x00')

    def write(self, str):
        prefix = 'FEA0'

        for c in str:
            data = prefix + hex(ord(c)).replace('0x', '')
            self._s.write(data.decode('hex'))
        self._s.flush()

    def close(self):
        self._s.close()

    def nextline(self):
        self._s.write(b'\xFE\x45\x40')

if __name__ == '__main__':
    s = LCDControl()
    s.clear()
    s.write('Hello')
    s.nextline()
    s.write('World')
    s.close()
