from Crypto.PublicKey import RSA
import binascii

def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")

	
ct = input("input the cipherkey: ")
ct2 = int(ct)

#this takes the input from the txt file called mykey3
recipient_key = RSA.import_key(open("mykey3").read())
print("p =", recipient_key.p)
print("q =", recipient_key.q)
print("e =", recipient_key.e)
print("n =", recipient_key.n)
print("d =", recipient_key.d)
#this is addeding the values from the txt files to veraibles in the code

p = recipient_key.p
q = recipient_key.q
e = recipient_key.e
n = recipient_key.n
d = recipient_key.d

#this is where the decryption is happening and print the flag in cleartext to be submitted
#on the website. 
decrypted = pow(ct2, d, n)   ## decrypt
plaintext = int2string(decrypted)
print()
print(("flag = ") + (plaintext))


