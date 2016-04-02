import struct

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
        out = struct.unpack(fmt, self.data[self.index : self.index + size])[0]
        self.index += size
        return out

    def size(self):
        size = ord(self.data[self.index])

        # 1 byte (no signature)
        if size & 128 == 0:
            self.index += 1
            return size

        sig = size >> 6

        # 2 bytes (signature is 10)
        if sig == 2:
            return self.uint16() & 0x3fff

        if sig == 3:
            return self.uint32() & 0x3fffffff

    def uint8(self):
        out = ord(self.data[self.index])
        self.index += 1
        return out

    def uint16(self):
        return self.__unpack('!H')

    def uint32(self):
        return self.__unpack('!I')

    def int8(self):
        return self.__unpack('!b')

    def int16(self):
        return self.__unpack('!h')

    def int32(self):
        return self.__unpack('!i')

    def float32(self):
        return self.__unpack('!f')

    def float64(self):
        return self.__unpack('!d')

    def bytes(self):
        size = self.size()
        out = self.data[self.index : self.index + size]
        self.index += size

        return out

    def string(self):
        return self.bytes().decode('utf-8')

class Encoder():
    def __init__(self):
        self.data = ''

    def __pack(self, fmt, value):
        self.data += struct.pack(fmt, value)

    def size(self, size):
        if size > 0x3fffffff:
            raise ArgumentError('Provided size is too long!')

        if size < 0x80:
            return self.uint8(size)

        if size < 0x4000:
            return self.uint16(size | 0x8000)

        return self.uint32(size | 0xc0000000)

    def uint8(self, value):
        self.data += chr(value)
        return self

    def uint16(self, value):
        self.__pack('!H', value)
        return self

    def uint32(self, value):
        self.__pack('!I', value)
        return self

    def int8(self, value):
        self.__pack('b', value)
        return self

    def int16(self, value):
        self.__pack('!h', value)
        return self

    def int32(self, value):
        self.__pack('!i', value)
        return self

    def float32(self, value):
        self.__pack('!f', value)
        return self

    def float64(self, value):
        self.__pack('!d', value)
        return self

    def bytes(self, value):
        size = len(value)
        self.size(size)
        self.data += value
        return self

    def string(self, value):
        self.bytes(value.encode('utf-8'))
        return self

    def end(self):
        return self.data
