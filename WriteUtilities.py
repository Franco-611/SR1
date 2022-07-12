import struct

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    #2 byte
    return struct.pack('=h', w)

def dword(d):
    #4 byte
    return struct.pack('=l', d)



