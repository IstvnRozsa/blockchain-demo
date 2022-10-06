import hashlib
import timeit
'''
#text = "hello".encode()
text = b"hello"

my_hash = hashlib.sha256(text)

print(my_hash.digest())
print(my_hash.hexdigest())
'''

'''
    Mining
'''
hash_ = hashlib.sha256(b"test")
start_time = timeit.default_timer()

difficulty = 6
nonce = 0

while hash_.hexdigest()[0:difficulty] != "0" * difficulty:
    hash_ = hashlib.sha256(("test" + str(nonce)).encode())
    nonce += 1

end_time = timeit.default_timer() - start_time
print(end_time)
print(nonce)
print(hash_.hexdigest())
'''
    Mining
'''