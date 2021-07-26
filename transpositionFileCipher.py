import time, os, sys, encryptTransposition, decryptTransposition

def main():
    #This is the file you want to encrypt
    inputFilename='frankenstein.txt'
    #BE CAREFUL! If a file with the outputFilename already exists, this program will overwrite that file
    outputFilename='frankenstein.encrypted.txt'
    myKey=10
    myMode='encrypt' #set to encrypt or decrypt
    #if the input file does not exist, the program terminates early
    if not os.path.exists(inputFilename):
        print('This file %s does not exist. Quitting...' %(inputFilename))
        sys.exit
    if os.path.exists(outputFilename):
        print('THis will overwrite the current file %s. (C)ontinue or (Q)uit?'%(outputFilename))
        response=input('> ')
        #if the user does not put 'C' (response.lower converts whatever response into lowercase letters)in the response, the program terminates
        if not response.lower().startswith('c'):
            sys.exit
    #opens the file that you want to encrypt, and sets it to fileObj
    fileObj=open(inputFilename)
    #sets the text in the file as the text that this program will encrypt
    content=fileObj.read()
    #closes the file
    fileObj.close()
    
    #this will print something like 'encrypting...'
    #the '.title' is for the program to make the first letter of every word in the variable to be uppercase
    print('%sing...'%(myMode.title()))
    #Measures how long the encryption takes
    startTime=time.time()
    #if the mode is 'encrypt', run the encryption program
    if myMode=='encrypt':
        translated=encryptTransposition.encryptMessage(myKey, content)
    #if the mode is 'decrypt', run the decryption program
    elif myMode=='decrypt':
        translated=decryptTransposition.decryptMessage(myKey, content)
    #variable for total time taken
    #'round()' to round up the decimal places 
    totalTime=round(time.time()-startTime, 2)
    #This prints something like 'Encrypt(ion) time: 5 seconds'
    print('%sion time: %s seconds'%(myMode.title(), totalTime))
    #The "W" means that you are opening the file with the purpose of writing to it
    outputFileObj=open(outputFilename, 'w')
    #Puts the translated code into the file
    outputFileObj.write(translated)
    #close the file
    outputFileObj.close()
    
    #This prints something like: 'Done encrypt(ing) (10 characters),'
    print('Done %sing %s (%s characters),' %(myMode, inputFilename, len(content)))
    #This prints something like: 'Encrypt(ed) file is frankenstein.encrypted.txt.'
    print('%sed file is %s.'%(myMode.title(), outputFilename))


main()
                                    
        
