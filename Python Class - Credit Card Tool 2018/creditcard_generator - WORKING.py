import random

#this is the section of the code where all the values that are needed are caluclated.
banksidnum = random.randint(100000, 999999)
month = random.randint(1, 12)
year = random.randint(19, 30)
genacardnum = random.randint(1000000000, 9999999999)
makecvv = random.randint(100, 999)
creditcard = str(banksidnum) + str(genacardnum)

#this is the lunh algorythm that is used to verify a credit card by checksum
#the details of this can be found in the Validator script

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

	
#This will print only if the luhn algorythm confirms that the card is correct valid
#this will generate the card number, a cvv number, a month of exipry and year of expiry
#these calculations do not work but are just random strings

if checksum == 0:
    print("")
    print(("Card Number: ") + str(banksidnum) + str(genacardnum))
    print(("CVV number: ") + str(makecvv))
    print(("month of Exipry: ") + str(month))
    print(("Year of Exipry: ") + str(year))
    print("The Card Passess Validation")
else:
    make_verify()

#if there is a failure to validate the card thent the program will run again
#and keep running generating new cards until it can generate a card that is
#vaild
