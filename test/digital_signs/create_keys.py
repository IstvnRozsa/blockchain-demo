import rsa

public_key, private_key = rsa.newkeys(1024)
name = "Bela"
with open(name + "_public.pem", "wb") as f:
    f.write(public_key.save_pkcs1("PEM"))

with open(name + "_private.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))


