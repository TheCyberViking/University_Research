import binascii
def string2int(my_str):
    return int(binascii.hexlify(my_str), 16)
def int2string(my_int):
    return binascii.unhexlify(format(my_int, "x").encode("utf-8")).decode("utf-8")
# -------------------------------------------------------------------------
n = 23516695565660963250242846975094031309572348962900032827958534374248114661507001374384417953124930587796472484525315334716723068326965228898857733318407681656604325744994115789416012096318656034667361976251100005599211469354510367804546831680730445574797161330145320706346512982316782618118878428893337849886890813813050423818145497040676697510093220374542784895778086554812954376689653727580227087363619223145837820593375994747273662064715654881379557354513619477314410917942381406981452545764657853425675230343749326640073923166795823683203941972393206970228647854927797483660176460658959810390117898333516129469397
e = 65537
d = 9587600726595591453426898215169101767863399178169979967502694355028996988583633210586039386751682566723132708455252764519220038491664005843242439790264046968625524201298469258242007220372280857992847470031480553726983707671745159488070659256258857978134570602562717609180653377092666963295822401721181836384326336158085408894694549470434424808812412260714422693522311366681659987060925945689943522825747715934700712908720597323076354591388316712970722935035250113120539406041972135508540472211484760814740089404942374666334486855389174327639061106567747152104666795257954039030591097174242386069752606041990644663125
p = 170436857437540785902894247445629309884819493988198726337160363787266132388801445377172350883259146330710518633323153950488107255453274647690833952071079266615535462115718628529996080297946386916054952930963525522668498855400580516951309863503734146131687670337990358661269686138903141878297721385390421204703
q = 137978932017559751745702136624874154954496829862527332457067512249687998333117572719846957168595861866495967632464915097378576596911015571165340454225721218087595428364080801400548238088288742249145662369868461078198744980520572785232341389134600070345564258064842348774203427257497319140459851255774165194699
ciphertext = 12060751446986145559753258604964288613009905939999612142364090162932784553289274985360758786650150438909964774489580594646537566480131089578622598287608280958826485540308546699201437758196408375494069165098540792161560520821702762571130453590350894456351542803892333747581478520236785140328470857700892653885938706372579150142033036479912415927913687580857324142121399292745144946430853334522298591089627330825281302600321017113877555269059227306217943736817867883165263245345825896646180907782570834990026416074994773400197992710509066779111650705105160806274734336871715369410205954061055784649468877193662056626998
## ----- decrypt cuphertext then convert number back to a string
decrypted = pow(ciphertext, d, n)   ## decrypt
plaintext = int2string(decrypted)
print (plaintext)