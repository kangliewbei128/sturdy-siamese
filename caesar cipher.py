import pyperclip
import string
#This asks the user for what message they want to be encrypted
inputedmessage=input('enter a message to be translated:')
#converts the message that the user inputed into lowercase letters. optional. If you want it converted, add .lower() at the end of inputedmessage
message=inputedmessage
#How far up the alphabet do you want the letter to change into (e.g A will go up 13 letters in the alphabet to M)
key=13
#DO you want to decrypt or encrypt the message?
mode='encrypt'
#THe symbols that you can convert the message into
SYMBOLS='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789!?,.'
#translated will be an empty string that values can be added to later
translated=''
#for each symbol in the message that you want to be translated
for symbol in message:
    #if the symbol is in SYMBOLS so that it can be encrypted
    if symbol in SYMBOLS:
        #.find(symbol) finds which position in numerics the symbol in message is in SYMBOLS (e.g A is t position 11 in SYMBOLS)
        #.find function will return a number
        symbolIndex=SYMBOLS.find(symbol)
        if mode=='encrypt':
            #This shifts the letter in the message up the alphabet. key is 13, so the letter will go up 13 letters. 
            #TranslatedIndex is the new position in which the letter is. (e.g after A gone up 13 alphabets to M, M is in position 26. translatedIndex=26)
            translatedIndex=symbolIndex+key
        elif mode=='decrypt':
            #since encrypt moves the letter up, to decrypt move the letter down.
            translatedIndex=symbolIndex-key
        if translatedIndex >= len(SYMBOLS):
            #if the position ends up going to more than 65, go back to the start,1 
            translatedIndex=translatedIndex-len(SYMBOLS)
        elif translatedIndex<=0:
            #THis happens in the case of decrypt. SO it will be go back to the end of SYMBOLS.
            translatedIndex=translatedIndex+len(SYMBOLS)
        #New translated message = what is in the translated variable now + the symbol in the position. THe square brackets are the index, so like for
        #helloworld[6] is 'O'
        translated=translated+SYMBOLS[translatedIndex]
    else:
        #If any of the symbols that the user try to put in is not in SYMBOLS, just dont encrypt that particular symbol and add it to what you can translate
        translated=translated+symbol
print(translated)
#This translated
pyperclip.copy(translated)
