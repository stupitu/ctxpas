import re, random

def CitrixDecode (encpas):
    decpas = ''
    l = re.findall('(.{2})',encpas)
    k = int(l[2], base=16)
    p = k^(k|67)
    for i in l[3:]:
        c = int(i, base=16)
        decpas += chr(c^p^k)
        p = c
    return decpas

def CitrixEncode(decpas, k = 91):
    if k == 91:
        k = random.randrange(256) 
    p = k^(k|67)
    e = '{:04x}'.format((len(decpas) + 1)) + '{:02x}'.format(k) 
    for i in decpas:
        c = ord(i)^p^k
        e += '{:02x}'.format(c)
        p = c
    return e

