#You must know how the transition cipher works like first!
#Main formula: currentIndex of box/position of word=column word is in + key*row number
#e.g currentIndex for words in column 2: (2+8), (2+16), (2+24), depending on how many roles there are.

#import the module that can help you copy the code onto your clipboard
import pyperclip

#here is the main function that will be executed. Notice that there is a function inside this function.
def main():
    myMessage=input('Enter code to be encrypted here: ')
    myKey=8
    #calling the function. myKey=key and myMessage=message
    #the variables inside the brackets of a function are the same even with ther name.
    #You can change the variables (also called parameters) as long as they are defined in that same order
    ciphertext=encryptMessage(myKey, myMessage)
    print('Here is your encrypted code:')
    print(ciphertext+'|')
    #copy your encrypted code to the clipboard.
    pyperclip.copy(ciphertext)

#This is the function that will do the encryption.
#main() function organizes the details.
def encryptMessage(key, message):
    #make 8 empty boxes to be filled in later.
    ciphertext=['']*key
    #This loop will repeat 8 times, for each column
    #column=key
    for column in range(key):
        #the while loop will repeat for each column. When one column is done, it will reset currentIndex to the number of the next column
        currentIndex=column
        #This will go encrypt every 8 letters in a sentence
        #e.g for 'Common sense is not common' -> letters ' C, e, n, o ' will be first to be encrypted because they are 8 letters apart.
        #Once the first set of the 8 letters are encrypted, the next set of 8 letters will be encrypted.

        #'lesser than the length of message' so that the loop will repeat for the next set of 8 letters when it gets to the last letter of the first set of 8 letters.
        while currentIndex<len(message):
            #For column 1, the first empty box of 'ciphertext' list will be called.
            #The empty box will be filled in with the encrypted letters, that is the first set of 8 letters.
            ciphertext[column]+=message[currentIndex]
            #There are 8 letters in every row, because there are 8 columns. Add 8 to the column and you will get to the next letter in the same column
            #After currentIndex has a new value, the letter will be encrypted
            #E.g for the 2nd letter in column 1, currentIndex=0+8 (python values start from 0).
            #The letter from the message('COmmon sense is not so common') will be the 8th letter, 'e'.
            #'e' will be put into the first box.
            #THis line is to move up the currentIndex number to the next letter in the same column.
            currentIndex+=key
    #all the letters are in their individual boxes in the ciphertext list.
    # .join() to put the letters into a single word
    return ''.join(ciphertext)

#call the main function to execute the code.
main()
    
