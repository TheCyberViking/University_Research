from sys import argv;
from tr import tr;
from time import sleep;

cipher = argv[1];
text = argv[2];
result = '';
diclenght = 0;


def makeallrots(temprots):
    for i in range(94): temprots += (chr(i + 33))
    return (temprots)


def makekey(n, diclenght, dictionary):
    key = ('')
    for i in range(diclenght):
        fix_number = (i + n)
        while (len(dictionary) <= fix_number): fix_number -= len(dictionary); sleep(0.0001)
        if (int(fix_number) == 12) & (str(cipher) == str('all')):
            key += ('\-');
        else:
            key += (dictionary[fix_number])
    return (key)


def runcipher(dictionary, diclenght):
    for i in range(diclenght): key = makekey(i, diclenght, dictionary); print(
        tr(dictionary, key, text))


def getciphers(rotall):
    if (str(cipher) == str('dec')):
        rot = 5; diclenght = 10; runcipher(rotall[15:15 + diclenght], diclenght)
    elif (str(cipher) == str('alpha') or str(cipher) == str('ceaser')):
        rot = 13; diclenght = 26; runcipher((str(rotall[97 - 33:97 + diclenght - 33]) + str(
            rotall[65 - 33:65 + diclenght - 33])), diclenght)
    elif (str(cipher) == str('all')):
        rot = 47; diclenght = 94; runcipher((rot), (rotall[0:diclenght]), diclenght)
    else:
        print('Unknown Cipher')

getciphers(makeallrots(''))
