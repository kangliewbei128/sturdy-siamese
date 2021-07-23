import math
import pyperclip

def main():
    myMessage=input('Enter the message you want to be decrypted here: ')
    myKey=8
    print('The key is 8.')
    plaintext = decryptMessage(myKey, myMessage)
    print('Here is your decrypted message: ')
    print(plaintext + '|')
    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    #math.ceil rounds the number up only. numofcolumns = length of message/key
    numofcolumns=int(math.ceil(len(message)/float(key)))
    numofrows=key
    #number of blank spaces = total boxes - boxes with characters in them
    numofshadedboxes=(numofcolumns*numofrows)-len(message)
    #creates empty boxes to put letters into them. THe decrypted code is read vertically down in columns
    plaintext=['']*numofcolumns
    column=0
    row=0
    #this loop is repeated for each letter in the messasge
    #each letter in the message is decrypted separately
    for symbol in message:
        #puts the letters into the empty boxes
        plaintext[column] +=symbol
        #goes to the next column and the next empty box
        column+=1
        #if the loop runs out of columns of meets a blank space in between letters in the code,
        #go back to the beginning (the first column) and make another row
        if (column == numofcolumns) or (column == numofcolumns-1 and row>= numofrows - numofshadedboxes):
            column=0
            row+=1
    return ''.join(plaintext)

main()
