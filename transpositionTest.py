import encryptTransposition
import decryptTransposition
import sys
import random

def main():
    random.seed(42)
    for i in range(20):
        message='QWERTYUIOPASDFGHJKLZXCVBNM'*random.randint(4,40)
        message=list(message)
        random.shuffle(message)
        message=''.join(message)
        print('Test #%s: "%s..." '%(i+1, message))
        for key in range(1,int(len(message)/2)):
            encrypted=encryptTransposition.encryptMessage(key,message)
            decrypted=decryptTransposition.decryptMessage(key,message)
            if message !=decrypted:
                print('Mismatch with key %s and message %s '%(key, message))
                print('Decrypted as '+decrypted)
                sys.exit
    print('Transposition cipher test passed')


main()
