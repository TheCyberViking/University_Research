from Crypto.PublicKey import RSA


recipient_key = RSA.import_key(open("mykey2").read())
#this is taking the input of the mykey2 file and reading it

print("n =", recipient_key.n)
print("d =", recipient_key.d)
print("e =", recipient_key.e)
#this sets the values in the txt to the needed veriables


print()
print("all together") #right now ........ over you.... bum bum buda bummmmm
flag = (recipient_key.n,recipient_key.e,recipient_key.d)
flagnoice = (str(flag)[1:-1])
flagnoicer = flagnoice.replace(" ", "")
flagnoicerer = flagnoicer.replace("(" and ")", "")
print("ZD{" + flagnoicerer + "}")

#this adds teh flag teogheter and pritns it out  as the flag string that was needed