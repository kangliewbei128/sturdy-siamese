#asks the user what code do they want to be decrypted
message=input("Enter the code that you want to be decrypted:")
#This list of symbols must be same as symbols in the encrypt program, if not when the letters are shifted it would not end up in the same position.
SYMBOLS='QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm123456789!?,.'
#The letters can be shifted up 65 times (65 is the length of SYMBOL).
#If letter is shifted up more than 65 times, e.g 66 times it will be equivalent to shifting it up one time because it will take one cycle about SYMBOL

#The program will try all keys for the length of SYMBOL. THe loop will repeat for each key.
for key in range(len(SYMBOLS)):
    #The end translated variable product is different each time this loop is ran. Thus, the variable must be introduced in the loop.
    translated=''
    #for each symbol in the code
    for symbol in message:
        #if the letter is in SYMBOLS , or else just add it to the end
        if symbol in SYMBOLS:
            #find the position of the letter in the original encrypted code. THis will return a number. (e.g W is in position 2, so symbolINdex=2)
            symbolIndex=SYMBOLS.find(symbol)
            #since the letter moves up in the caesar cipher, to decrypt it move the letter down. (e.g Move T down 5 position (key=5), it will be Q.
            #Q is in position 1 so translatedIndex=1)
            translatedIndex=symbolIndex-key
            #the letters will go back around to the end of SYMBOL which is the symbol '.'
            #if moving the letter down makes the letter go off range
            if translatedIndex<0:
                translatedIndex=translatedIndex+len(SYMBOLS)
            #new decrypted code is:
            #this line of program will repeat for each letter. so everytime "translated" will get a new value and keep building up to the end of the word.
            translated=translated+SYMBOLS[translatedIndex]
        else:
            translated=translated+symbol
        #print the translated message.
        print('key #%s: %s '%(key, translated))
