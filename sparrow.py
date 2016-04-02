class Decoder:
    def __init__(self, data):
        if data == None or type(data) != str:
            raise ArgumentError('Invalid type')

        self.data = data
        self.index = 0
        self.boolIndex = -1
        self.boolShift = 0

    def __unpack(self, fmt):
        size = struct.calcsize(fmt)
        out = struct.unpack(fmt, self.data[index : index + size])
        self.index += size
        return out

    def __size(self):
        size = ord(self.data[self.index])

        # 1 byte (no signature)
        if size & 128 == 0:
            self.index += 1
            return size

        sig = size >>> 6

        # 2 bytes (signature is 10)
        if sig == 2:
            return self.uint16() & 0x3fff

        if sig == 4:
            return self.uint32 & 0x3fffffff

    def uint8(self):
        out = ord(self.data[self.index])
        self.index += 1
        return out

    def uint16(self):
        return self.__unpack('H')

    def uint32(self):
        return self.__unpack('I')

    def int8(self):
        return self.__unpack('b')

    def int16(self):
        return self.__unpack('h')

    def int32(self):
        return self.__unpack('i')

    def float32(self):
        return self.__unpack('f')

    def float64(self):
        return self.__unpack('d')

    def bytes(self):
        size = self.__size()
        out = self.data[self.index : self.index + size]
        self.index += size

        return out



class Encoder():
    def __init__(self):
        self.data = ''

    def __pack(self, fmt, value):
        self.data += struct.pack(fmt, data)

    def uint8(self, value):
        self.data += chr(value)
        return self

    def uint16(self, value):
        self.__pack('H', value)
        return self

    def uint32(self, value):
        self.__pack('I', value)
        return self

    def int8(self, value):
        self.__pack('b', value)
        return self

    def int16(self, value):
        self.__pack('h', value)
        return self

    def int32(self, value):
        self.__pack('i', value)
        return self

    def float32(self, value):
        self.__pack('f', value)
        return self

    def float64(self, value):
        self.__pack('d', value)
        return self
