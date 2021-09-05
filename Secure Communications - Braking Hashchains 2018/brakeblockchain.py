import hashlib

#below is the known hash for the ECSC after being computed in a block chain
#our goal is the find the hash that is before this hash on the compute list

knownhash = "c89aa2ffb9edcc6604005196b5f0e0e4" 
ecsc = b"ecsc"

#known hash "seed" and original input 

#bellow is the section of code using the hash library in python to hash ecsc in md5
m = hashlib.md5(ecsc)
count = 1
print(knownhash + " " + m.hexdigest())
a = []


#bellow is the section of code using the hash library in python to hash ecsc in md5
#this seciton of the code that will keep re hashing ecsc md5 until it gets a hash that machines

while(m.hexdigest() != knownhash):
	m = hashlib.md5(m.hexdigest().encode("utf-8"))
	count += 1
	a.append(m.hexdigest())
	print(m.hexdigest() + " + " + str(knownhash) + " : " + str(count))

	
	
print("2nd last hash for ECSC: " + a[len(a) - 2])

#after hashing is complete it will print the 2nd last hash here by just taking the last form the list