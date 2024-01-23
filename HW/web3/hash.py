import hashlib

p = '1234'.encode()
h = hashlib.md5(p)
print(len(h.hexdigest()))
