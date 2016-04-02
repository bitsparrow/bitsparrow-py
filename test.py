#coding: utf-8

import unittest
import math

import bitsparrow

def bytes_to_str(bytes):
    return ''.join([chr(x) for x in bytes])

expected_buf = bytes_to_str([
  0xc8,0x23,0x29,0x49,0x96,0x02,0xd2,0xd6,0x8a,0xd0,0xb6,0x69,0xfd,
  0x2e,0x0f,0x42,0x69,0x74,0x53,0x70,0x61,0x72,0x72,0x6f,0x77,0x20,
  0xf0,0x9f,0x90,0xa6,0x83,0x69,0x53,0x70,0x61,0x72,0x72,0x6f,0x77,
  0x20,0x2f,0xcb,0x88,0x73,0x70,0x65,0x72,0x2e,0x6f,0xca,0x8a,0x2f,
  0x0a,0x0a,0x55,0x6e,0x64,0x65,0x72,0x20,0x74,0x68,0x65,0x20,0x63,
  0x6c,0x61,0x73,0x73,0x69,0x66,0x69,0x63,0x61,0x74,0x69,0x6f,0x6e,
  0x20,0x75,0x73,0x65,0x64,0x20,0x69,0x6e,0x20,0x74,0x68,0x65,0x20,
  0x48,0x61,0x6e,0x64,0x62,0x6f,0x6f,0x6b,0x20,0x6f,0x66,0x20,0x74,
  0x68,0x65,0x20,0x42,0x69,0x72,0x64,0x73,0x20,0x6f,0x66,0x20,0x74,
  0x68,0x65,0x20,0x57,0x6f,0x72,0x6c,0x64,0x20,0x28,0x48,0x42,0x57,
  0x29,0x20,0x6d,0x61,0x69,0x6e,0x20,0x67,0x72,0x6f,0x75,0x70,0x69,
  0x6e,0x67,0x73,0x20,0x6f,0x66,0x20,0x74,0x68,0x65,0x20,0x73,0x70,
  0x61,0x72,0x72,0x6f,0x77,0x73,0x20,0x61,0x72,0x65,0x20,0x74,0x68,
  0x65,0x20,0x74,0x72,0x75,0x65,0x20,0x73,0x70,0x61,0x72,0x72,0x6f,
  0x77,0x73,0x20,0x28,0x67,0x65,0x6e,0x75,0x73,0x20,0x50,0x61,0x73,
  0x73,0x65,0x72,0x29,0x2c,0x20,0x74,0x68,0x65,0x20,0x73,0x6e,0x6f,
  0x77,0x66,0x69,0x6e,0x63,0x68,0x65,0x73,0x20,0x28,0x74,0x79,0x70,
  0x69,0x63,0x61,0x6c,0x6c,0x79,0x20,0x6f,0x6e,0x65,0x20,0x67,0x65,
  0x6e,0x75,0x73,0x2c,0x20,0x4d,0x6f,0x6e,0x74,0x69,0x66,0x72,0x69,
  0x6e,0x67,0x69,0x6c,0x6c,0x61,0x29,0x2c,0x20,0x61,0x6e,0x64,0x20,
  0x74,0x68,0x65,0x20,0x72,0x6f,0x63,0x6b,0x20,0x73,0x70,0x61,0x72,
  0x72,0x6f,0x77,0x73,0x20,0x28,0x50,0x65,0x74,0x72,0x6f,0x6e,0x69,
  0x61,0x20,0x61,0x6e,0x64,0x20,0x74,0x68,0x65,0x20,0x70,0x61,0x6c,
  0x65,0x20,0x72,0x6f,0x63,0x6b,0x66,0x69,0x6e,0x63,0x68,0x29,0x2e,
  0x20,0x54,0x68,0x65,0x73,0x65,0x20,0x67,0x72,0x6f,0x75,0x70,0x73,
  0x20,0x61,0x72,0x65,0x20,0x73,0x69,0x6d,0x69,0x6c,0x61,0x72,0x20,
  0x74,0x6f,0x20,0x65,0x61,0x63,0x68,0x20,0x6f,0x74,0x68,0x65,0x72,
  0x2c,0x20,0x61,0x6e,0x64,0x20,0x61,0x72,0x65,0x20,0x65,0x61,0x63,
  0x68,0x20,0x66,0x61,0x69,0x72,0x6c,0x79,0x20,0x68,0x6f,0x6d,0x6f,
  0x67,0x65,0x6e,0x65,0x6f,0x75,0x73,0x2c,0x20,0x65,0x73,0x70,0x65,
  0x63,0x69,0x61,0x6c,0x6c,0x79,0x20,0x50,0x61,0x73,0x73,0x65,0x72,
  0x2e,0x5b,0x34,0x5d,0x20,0x53,0x6f,0x6d,0x65,0x20,0x63,0x6c,0x61,
  0x73,0x73,0x69,0x66,0x69,0x63,0x61,0x74,0x69,0x6f,0x6e,0x73,0x20,
  0x61,0x6c,0x73,0x6f,0x20,0x69,0x6e,0x63,0x6c,0x75,0x64,0x65,0x20,
  0x74,0x68,0x65,0x20,0x73,0x70,0x61,0x72,0x72,0x6f,0x77,0x2d,0x77,
  0x65,0x61,0x76,0x65,0x72,0x73,0x20,0x28,0x50,0x6c,0x6f,0x63,0x65,
  0x70,0x61,0x73,0x73,0x65,0x72,0x29,0x20,0x61,0x6e,0x64,0x20,0x73,
  0x65,0x76,0x65,0x72,0x61,0x6c,0x20,0x6f,0x74,0x68,0x65,0x72,0x20,
  0x41,0x66,0x72,0x69,0x63,0x61,0x6e,0x20,0x67,0x65,0x6e,0x65,0x72,
  0x61,0x20,0x28,0x6f,0x74,0x68,0x65,0x72,0x77,0x69,0x73,0x65,0x20,
  0x63,0x6c,0x61,0x73,0x73,0x69,0x66,0x69,0x65,0x64,0x20,0x61,0x6d,
  0x6f,0x6e,0x67,0x20,0x74,0x68,0x65,0x20,0x77,0x65,0x61,0x76,0x65,
  0x72,0x73,0x2c,0x20,0x50,0x6c,0x6f,0x63,0x65,0x69,0x64,0x61,0x65,
  0x29,0x5b,0x34,0x5d,0x20,0x77,0x68,0x69,0x63,0x68,0x20,0x61,0x72,
  0x65,0x20,0x6d,0x6f,0x72,0x70,0x68,0x6f,0x6c,0x6f,0x67,0x69,0x63,
  0x61,0x6c,0x6c,0x79,0x20,0x73,0x69,0x6d,0x69,0x6c,0x61,0x72,0x20,
  0x74,0x6f,0x20,0x50,0x61,0x73,0x73,0x65,0x72,0x2e,0x5b,0x35,0x5d,
  0x20,0x41,0x63,0x63,0x6f,0x72,0x64,0x69,0x6e,0x67,0x20,0x74,0x6f,
  0x20,0x61,0x20,0x73,0x74,0x75,0x64,0x79,0x20,0x6f,0x66,0x20,0x6d,
  0x6f,0x6c,0x65,0x63,0x75,0x6c,0x61,0x72,0x20,0x61,0x6e,0x64,0x20,
  0x73,0x6b,0x65,0x6c,0x65,0x74,0x61,0x6c,0x20,0x65,0x76,0x69,0x64,
  0x65,0x6e,0x63,0x65,0x20,0x62,0x79,0x20,0x4a,0x6f,0x6e,0x20,0x46,
  0x6a,0x65,0x6c,0x64,0x73,0xc3,0xa5,0x20,0x61,0x6e,0x64,0x20,0x63,
  0x6f,0x6c,0x6c,0x65,0x61,0x67,0x75,0x65,0x73,0x2c,0x20,0x74,0x68,
  0x65,0x20,0x63,0x69,0x6e,0x6e,0x61,0x6d,0x6f,0x6e,0x20,0x69,0x62,
  0x6f,0x6e,0x20,0x6f,0x66,0x20,0x74,0x68,0x65,0x20,0x50,0x68,0x69,
  0x6c,0x69,0x70,0x70,0x69,0x6e,0x65,0x73,0x2c,0x20,0x70,0x72,0x65,
  0x76,0x69,0x6f,0x75,0x73,0x6c,0x79,0x20,0x63,0x6f,0x6e,0x73,0x69,
  0x64,0x65,0x72,0x65,0x64,0x20,0x74,0x6f,0x20,0x62,0x65,0x20,0x61,
  0x20,0x77,0x68,0x69,0x74,0x65,0x2d,0x65,0x79,0x65,0x2c,0x20,0x69,
  0x73,0x20,0x61,0x20,0x73,0x69,0x73,0x74,0x65,0x72,0x20,0x74,0x61,
  0x78,0x6f,0x6e,0x20,0x74,0x6f,0x20,0x74,0x68,0x65,0x20,0x73,0x70,
  0x61,0x72,0x72,0x6f,0x77,0x73,0x20,0x61,0x73,0x20,0x64,0x65,0x66,
  0x69,0x6e,0x65,0x64,0x20,0x62,0x79,0x20,0x74,0x68,0x65,0x20,0x48,
  0x42,0x57,0x2e,0x20,0x54,0x68,0x65,0x79,0x20,0x74,0x68,0x65,0x72,
  0x65,0x66,0x6f,0x72,0x65,0x20,0x63,0x6c,0x61,0x73,0x73,0x69,0x66,
  0x79,0x20,0x69,0x74,0x20,0x61,0x73,0x20,0x69,0x74,0x73,0x20,0x6f,
  0x77,0x6e,0x20,0x73,0x75,0x62,0x66,0x61,0x6d,0x69,0x6c,0x79,0x20,
  0x77,0x69,0x74,0x68,0x69,0x6e,0x20,0x50,0x61,0x73,0x73,0x65,0x72,
  0x69,0x64,0x61,0x65,0x2e,0x5b,0x35,0x5d,0x06,0x01,0x02,0x03,0x04,
  0x05,0x06,0x64,0xa7,0x10,0xc0,0x0f,0x42,0x40,0xff,0xff,0xff,0xff,
  0x40,0x49,0x0f,0xdb,0x40,0x09,0x21,0xfb,0x54,0x44,0x2d,0x18
])

long_text = u"Sparrow /ˈsper.oʊ/\n\nUnder the classification used in the Handbook of the Birds of the World (HBW) main groupings of the sparrows are the true sparrows (genus Passer), the snowfinches (typically one genus, Montifringilla), and the rock sparrows (Petronia and the pale rockfinch). These groups are similar to each other, and are each fairly homogeneous, especially Passer.[4] Some classifications also include the sparrow-weavers (Plocepasser) and several other African genera (otherwise classified among the weavers, Ploceidae)[4] which are morphologically similar to Passer.[5] According to a study of molecular and skeletal evidence by Jon Fjeldså and colleagues, the cinnamon ibon of the Philippines, previously considered to be a white-eye, is a sister taxon to the sparrows as defined by the HBW. They therefore classify it as its own subfamily within Passeridae.[5]";

bytes = bytes_to_str([1, 2, 3, 4, 5, 6])

class EncoderTests(unittest.TestCase):
    def test_eat_own_bird_food(self):
        buf = bitsparrow.Encoder()\
            .uint8(200)\
            .uint16(9001)\
            .uint32(1234567890)\
            .int8(-42)\
            .int16(-30000)\
            .int32(-1234567890)\
            .string(u'BitSparrow 🐦')\
            .string(long_text)\
            .bytes(bytes)\
            .size(100)\
            .size(10000)\
            .size(1000000)\
            .size(1073741823)\
            .float32(math.pi)\
            .float64(math.pi)\
            .end()

        self.assertEqual(buf, expected_buf)

class DecoderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.decoder = bitsparrow.Decoder(expected_buf)

    def test_01_unit8(self):
        self.assertEqual(self.decoder.uint8(), 200)

    def test_02_unit16(self):
        self.assertEqual(self.decoder.uint16(), 9001)

    def test_03_unit32(self):
        self.assertEqual(self.decoder.uint32(), 1234567890)

    def test_04_int8(self):
        self.assertEqual(self.decoder.int8(), -42)

    def test_05_int16(self):
        self.assertEqual(self.decoder.int16(), -30000)

    def test_06_int32(self):
        self.assertEqual(self.decoder.int32(), -1234567890)

    def test_07_string(self):
        self.assertEqual(self.decoder.string(), u'BitSparrow 🐦')

    def test_08_string_long_text(self):
        self.assertEqual(self.decoder.string(), long_text)

    def test_09_bytes(self):
        self.assertEqual(self.decoder.bytes(), bytes)

    def test_10_size(self):
        self.assertEqual(self.decoder.size(), 100)

    def test_11_size(self):
        self.assertEqual(self.decoder.size(), 10000)

    def test_12_size(self):
        self.assertEqual(self.decoder.size(), 1000000)

    def test_13_size(self):
        self.assertEqual(self.decoder.size(), 1073741823)

    def test_14_float32(self):
        self.assertTrue(self.decoder.float32() - math.pi < 0.0001)

    def test_15_float64(self):
        self.assertEqual(self.decoder.float64(), math.pi)

if __name__ == '__main__':
    unittest.main()