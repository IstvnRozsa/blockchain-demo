import hashlib

#text = "hello".encode()
text = b"hello"

my_hash = hashlib.sha256(text)

print(my_hash.digest())
print(my_hash.hexdigest())