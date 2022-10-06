import rsa
import json

with open("Bela_private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())
    
with open("Bela_public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

message = "Hello Bello"


# Encrypt and Decrypt a message
encrypted_message = rsa.encrypt(message.encode(), public_key)
print(encrypted_message)

decrypt_message = rsa.decrypt(encrypted_message, private_key)
print(decrypt_message)


# Sign a Message
message = {
    "amount": 20,
    "from": str(public_key),
    "to": "to"
}



print("-"*30)
signature = rsa.sign(json.dumps(message).encode(), private_key, "SHA-256")

try:
   #rsa.verify(json.dumps(message).encode(), b"xy", public_key)
    rsa.verify(json.dumps(message).encode(), signature, public_key)
    print("verified")
except rsa.VerificationError:
    print("Not verified")
print(signature)
print(json.dumps(message))
