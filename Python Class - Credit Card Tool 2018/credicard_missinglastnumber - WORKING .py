print()
print("##### Partial Card CheckSum #####")
print()
checkpar = input(str("input a Partial Credit Card Number: "))
print()
checked1 = False


#checksum of the card using the luhn algorithm for calculation
#the chard algorithm was found in an old infographic
def checker():
    a2 = 0
    a = str(int(checkpar[0]) * 2)
    b = str(int(checkpar[2]) * 2)
    c = str(int(checkpar[4]) * 2)
    d = str(int(checkpar[6]) * 2)
    e = str(int(checkpar[8]) * 2)
    f = str(int(checkpar[10]) * 2)
    g = str(int(checkpar[12]) * 2)
    h = str(int(checkpar[14]) * 2)
    ah = str(a + b + c + d + e + f + g + h)
    for i in range(len(ah)):
        a2 += int(ah[i])

    a1 = int(checkpar[1])
    b1 = int(checkpar[3])
    c1 = int(checkpar[5])
    d1 = int(checkpar[7])
    e1 = int(checkpar[9])
    f1 = int(checkpar[11])
    g1 = int(checkpar[13])
    h1 = int(checkpar[15])
    fin = int(a2 + a1 + b1 + c1 + d1 + e1 + f1 + g1 + h1)
    checksum = int(fin % 10)

	
    if checksum == 0:
        print("The card is Now Valid")
        print(("This is the Card Number: ") + (str(checkpar)))
        return(True)
    else:
        return(False)



#if card is 15 digits, add number to the end and run trough the checker fucntion to
#to add on the number to be able to verify
#This works by adding 1 number to the end and uping it in incromints until the card
#passes verificaiton
while checked1 == False:
    if len(checkpar) == (15):
        checkpar = checkpar + '0'
        checked1 = checker()
    elif len(checkpar) == (16):
        checkpar =  (checkpar[:15] + str(int(checkpar[15])+1))
        checked1 = checker()
        if (checkpar[15]==9 and checked1 == False):
            print('Not a valid Card Number')
            break

			
    else:
        print("please Enter a Card Number missing the last digit") #error response
        break