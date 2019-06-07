import machine


class accel():
    def __init__(self, i2c, addr=0x68):
        self.iic = i2c
        self.addr = addr
        self.iic.start()
        self.iic.writeto(self.addr, bytearray([107, 0]))
        self.iic.stop()
        self.counter = 0

    def get_raw_values(self):
        self.iic.start()
        a = self.iic.readfrom_mem(self.addr, 0x3B, 14)
        self.iic.stop()
        return a

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def get_values(self):
        raw_ints = self.get_raw_values()
        global counter
        vals = {}
        vals["idx"] = self.counter
        vals["accX"] = self.bytes_toint(raw_ints[0], raw_ints[1])
        vals["accY"] = self.bytes_toint(raw_ints[2], raw_ints[3])
        vals["accZ"] = self.bytes_toint(raw_ints[4], raw_ints[5])
        vals["tmp"] = self.bytes_toint(
            raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        vals["gyX"] = self.bytes_toint(raw_ints[8], raw_ints[9])
        vals["gyY"] = self.bytes_toint(raw_ints[10], raw_ints[11])
        vals["gyZ"] = self.bytes_toint(raw_ints[12], raw_ints[13])
        self.counter = self.counter + 1
        return vals  # returned in range of Int16
        # -32768 to 32767

    def val_test(self):  # ONLY FOR TESTING! Also, fast reading sometimes crashes IIC
        from time import sleep
        while 1:
            print(self.get_values())
            sleep(0.05)
