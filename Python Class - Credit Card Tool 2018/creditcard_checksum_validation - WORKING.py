creditcard = input("Please Enter your 16 Digit Credit Card Number: ")


#bellow is the calulation of the Luhn algoryotm that verifies if the card is correct
#this multiples the even possition numbers by 2

a2 = 0
a = str(int(creditcard[0]) * 2)
b = str(int(creditcard[2]) * 2)
c = str(int(creditcard[4]) * 2)
d = str(int(creditcard[6]) * 2)
e = str(int(creditcard[8]) * 2)
f = str(int(creditcard[10]) * 2)
g = str(int(creditcard[12]) * 2)
h = str(int(creditcard[14]) * 2)
ah = str(a + b + c + d + e + f + g + h)

#this the adds on the odd positons numbers to the original calculated number

for i in range(len(ah)):
    a2 += int(ah[i])
    a1 = int(creditcard[1])
    b1 = int(creditcard[3])
    c1 = int(creditcard[5])
    d1 = int(creditcard[7])
    e1 = int(creditcard[9])
    f1 = int(creditcard[11])
    g1 = int(creditcard[13])
    h1 = int(creditcard[15])
    fin = int(a2 + a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1)
    checksum = int(fin % 10)
	
#the moduls of the number is even then the check is verified, if it is odd then it is
#not a verifiedable card

if checksum == 0:
    print("The Credit Card is Valid")
else:
    print("The Credit Card Failed Validation")