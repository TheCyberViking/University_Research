print("")
creditcard = input(str("input a credit card number: "))
print("")
print("#######################################################")
print(("Entered Card Number: ") + (creditcard))
print("#######################################################")
print("")
checkedsum = False
industry = False
validbank = False

#this check does 3 things, it both validates the luhn algorythm
#it also tells the industry the card comes from
#and it also tells if the card is from a certain provider such as 
#mastercard, visa, debit and so on


# INDUSTRY CHECKER - this is to check the industry from which the card comes
if len(creditcard) == 16:
    if creditcard[0] in ('1', '2'):
        print("Card From: Airline Industry")
        industry = True
    elif creditcard[0] in ('3'):
        print("Card From: Travel and Entertainment Industry")
        industry = True
    elif creditcard[0] in ('4', '5'):
        print("Card From: Branking and Financial Industry")
        industry = True
    elif creditcard[0] in ('6'):
        print("Card From: Merchandizing and Banking Industry")
        industry = True
    elif creditcard[0] in ('7'):
        print("Card From: Petroleum Industry")
        industry = True
    elif creditcard[0] in ('8'):
        print("Card From: Telecom Industry")
        industry = True
    elif creditcard[0] in ('3'):
        print("Card From: National Assignment i.e. GOV")
        industry = True
    else:
        print("Unknown Industry Identifier")
elif len(creditcard) == 19:
    if creditcard[0] in ('1', '2'):
        print("Card From: Airline Industry")
        industry = True
    elif creditcard[0] in ('3'):
        print("Card From: Travel and Entertainment Industry")
        industry = True
    elif creditcard[0] in ('4', '5'):
        print("Card From: Branking and Financial Industry")
        industry = True
    elif creditcard[0] in ('6'):
        print("Card From: Merchandizing and Banking Industry")
        industry = True
    elif creditcard[0] in ('7'):
        print("Card From: Petroleum Industry")
        industry = True
    elif creditcard[0] in ('8'):
        print("Card From: Telecom Industry")
        industry = True
    elif creditcard[0] in ('9'):
        print("Card From: National Assignment i.e. GOV")
        industry = True
    else:
        print("Unknown Industry Identifier")

# ACCOUNT ISSUER CHECK - this checks for the card suplier i.e. visa, mastercard
if len(creditcard) == 16:
    if creditcard[0] in ('4'):
        print("Card is: Visa")
        validbank = True
    elif creditcard[0:2] in ('34'):
        print("Card is: American Express")
        validbank = True
    elif creditcard[0:2] in ('37'):
        print("Card is: American Express")
        validbank = True
    elif creditcard[0:2] in ('31'):
        print("Card is: China T Union")
        validbank = True
    elif creditcard[0:2] in ('62'):
        print("Card is: China UnionPay")
        validbank = True
    elif creditcard[0:2] in ('36'):
        print("Card is: Dinners Club Internationa")
        validbank = True
    elif creditcard[0:2] in ('55'):
        print("Card is: Diners Club USA MasterCard")
        validbank = True
    elif creditcard[0:2] in ('54'):
        print("Card is: Diners Club USA MasterCard")
        validbank = True
    elif creditcard[0:4] in ('6011'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:2] in ('64'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:2] in ('65'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:2] in ('60'):
        print("Card is: RuPay")
        validbank = True
    elif creditcard[0:4] in ('6521'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:4] in ('6522'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:3] in ('636'):
        print("Card is: InterPayment")
        validbank = True
    elif creditcard[0:3] in ('637'):
        print("Card is: InstaPayment")
        validbank = True
    elif creditcard[0:4] in ('3528'):
        print("Card is: JCB")
        validbank = True
    elif creditcard[0:2] in ('3589'):
        print("Card is: JCB")
        validbank = True
    elif creditcard[0:2] in ('50'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:2] in ('56'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:2] in ('58'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:3] in ('639'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:2] in ('67'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:4] in ('5019'):
        print("Card is: Dankort")
        validbank = True
    elif creditcard[0:4] in ('4571'):
        print("Card is: Dankort")
        validbank = True
    elif creditcard[0:4] in ('2200'):
        print("Card is: MIR")
        validbank = True
    elif creditcard[0:4] in ('2204'):
        print("Card is: MIR")
        validbank = True
    elif creditcard[0:6] in ('222100'):
        print("Card is: MasterCard")
        validbank = True
    elif creditcard[0:6] in ('272099'):
        print("Card is: MasterCard")
        validbank = True
    elif creditcard[0:2] in ('51'):
        print("Card is: MasterCard")
        validbank = True
    elif creditcard[0:2] in ('55'):
        print("Card is: Mastercard")
        validbank = True
    elif creditcard[0:4] in ('6334'):
        print("Card is: SOLO")
        validbank = True
    elif creditcard[0:4] in ('6767'):
        print("Card is: SOLO")
        validbank = True
    elif creditcard[0:1] in ('1'):
        print("Card is: UATP")
        validbank = True
elif len(creditcard) == 19:
    if creditcard[0] in ('4'):
        print("Card is: Visa")
        validbank = True
    elif creditcard[0:2] in ('34'):
        print("Card is: American Express")
        validbank = True
    elif creditcard[0:2] in ('37'):
        print("Card is: American Express")
        validbank = True
    elif creditcard[0:2] in ('31'):
        print("Card is: China T Union")
        validbank = True
    elif creditcard[0:2] in ('62'):
        print("Card is: China UnionPay")
        validbank = True
    elif creditcard[0:2] in ('36'):
        print("Card is: Dinners Club Internationa")
        validbank = True
    elif creditcard[0:2] in ('55'):
        print("Card is: Diners Club USA MasterCard")
        validbank = True
    elif creditcard[0:2] in ('54'):
        print("Card is: Diners Club USA MasterCard")
        validbank = True
    elif creditcard[0:4] in ('6011'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:2] in ('64'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:2] in ('65'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:2] in ('60'):
        print("Card is: RuPay")
        validbank = True
    elif creditcard[0:4] in ('6521'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:4] in ('6522'):
        print("Card is: Discover Card")
        validbank = True
    elif creditcard[0:3] in ('636'):
        print("Card is: InterPayment")
        validbank = True
    elif creditcard[0:3] in ('637'):
        print("Card is: InstaPayment")
        validbank = True
    elif creditcard[0:4] in ('3528'):
        print("Card is: JCB")
        validbank = True
    elif creditcard[0:2] in ('3589'):
        print("Card is: JCB")
        validbank = True
    elif creditcard[0:2] in ('50'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:2] in ('56'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:2] in ('58'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:3] in ('639'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:2] in ('67'):
        print("Card is: Maestro")
        validbank = True
    elif creditcard[0:4] in ('5019'):
        print("Card is: Dankort")
        validbank = True
    elif creditcard[0:4] in ('4571'):
        print("Card is: Dankort")
        validbank = True
    elif creditcard[0:4] in ('2200'):
        print("Card is: MIR")
        validbank = True
    elif creditcard[0:4] in ('2204'):
        print("Card is: MIR")
        validbank = True
    elif creditcard[0:6] in ('222100'):
        print("Card is: MasterCard")
        validbank = True
    elif creditcard[0:6] in ('272099'):
        print("Card is: MasterCard")
        validbank = True
    elif creditcard[0:2] in ('51'):
        print("Card is: MasterCard")
        validbank = True
    elif creditcard[0:2] in ('55'):
        print("Card is: Mastercard")
        validbank = True
    elif creditcard[0:4] in ('6334'):
        print("Card is: SOLO")
        validbank = True
    elif creditcard[0:4] in ('6767'):
        print("Card is: SOLO")
        validbank = True
    elif creditcard[0:1] in ('1'):
        print("Card is: UATP")
        validbank = True
	elif creditcard[0:6] in ["459654"]:
        print("Revolut Visa Debit Card")
		validbank = True
    elif creditcard[0:6] in ["539123"]:
        print("Revolut MasterCard Debit Card")
		validbank = True
	
	

#this is an added checker that I found online that will
#tell you what country the card is from if it falls into 
#these categories.

if creditcard[0:4] in ('4319'):
    print("The Card is From Ireland")
elif creditcard[0:2] in ('34') or creditcard[0:2] in ('37'):
    print("The Card is From America")
elif creditcard[0:2] in ('31'):
    print("The Card is from China")
elif creditcard[0:2] in ('62'):
    print("The Card is From China")
elif creditcard[0:2] in ('36'):
    print("The Card is International")
elif creditcard[0:3] in range(300,305):
    print("The Card is International")
elif creditcard[0:2] in range(54,55):
    print("The Card is from America")



# CHECKSUM - this is for checking the value of the card
# the calculation is every even list number * 2 then added to the odd number
# then devided by 10 to see if it becomes an even number
# if it is not even then that card fails checksum

if len(creditcard) == 16:
    a2=0
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
#    print(checksum)

    if checksum == 0:
        print("Checksum: Confirmed")
        checkedsum = True

# elif len(creditcard) == 19:


if industry == True and validbank == True and checkedsum == True:
    print("The Given Card is Valid")
elif industry == True and validbank == True:
    print('checkedsum: Failed')


else:
    print("The Number you entered was to short, you entered")
    print(len(creditcard))
    print("Numbers, The Number should be 16 or 19 Numbers in length")

#this is the fail safe so if something goes wrong it will default to these two messages
#it will also list the size of the inputed card to give an idea of card entereted
