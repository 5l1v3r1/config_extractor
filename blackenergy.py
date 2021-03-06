# Malware.lu
import sys
import string

def arc4(key, data):
    x = 0
    box = range(256)
    for i in range(256):
        box[i] = (box[i] ^ ord(key[i % len(key)])) % 256

    x = y = 0
    out = []
    for char in data:
        x = (x + 1) % 256
        y = (y + box[x]) % 256
        box[x], box[y] = box[y], box[x]
        out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

    return ''.join(out)

if __name__ == "__main__":
    fp = open(sys.argv[1])
    fp.seek(0x10)
    key = fp.read(0x10)
    data = fp.read()
    data = arc4(key, data)
    sys.stdout.write(data)
