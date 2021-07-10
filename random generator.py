import random
import string

girlnames=['Allie','Alina','Alsie','Aaron','Amber','Bella','Bellsie',
'Candice','Kenya','June','Kodi','Rosalie','Susannah','Taryn','Inez','Maia','Millie','Bertha','Leah',
'Pippa','Eva','Miriam','Autumn','Nadia','Tianna','Lillian','Christiana',
'Zara']
boynames=['Blaise','Kyron','Jaxon','Jason','Mike','Levy','Tanner',
'Jeffery','Lucian','Keenan','Naveed','Raphael','Herbert','Hubert','Chase',
'Kyle','Myles','Cole','Marco','Edgar','Melvin','Edward','Nathan','Tristan','Zach']
def name():
    gender=input('Press F for a girl\'s name and B for a boy\'s name:')
    print('name:')
    if gender=='F':
        chosenname1=random.choice(girlnames)
        print(chosenname1)
    elif gender=='B':
        chosenname2=random.choice(boynames)
        print(chosenname2)

name()

telephonenumber=string.digits
print('telephone number:')
for i in range(8):
    telephonenumber2=random.choice(telephonenumber)
    print(telephonenumber2, end='')


num=string.digits
words=['rtybows','krganroo','plitaes','kioprty','kiraart','ghetjk',
'cinnrmon','drftqy','metrplis','mnicallyr','jssieg',
'ctadnrnia','cqlifinia','dandlnie','roquetche','pqnyfle','coprosma',
'cffrered','']
print('\nusername:')
chosenword=str(random.choice(words))
separator=''
chosennumber=str(separator.join(random.choices(num)))
chosennumber2=str(separator.join(random.choices(num)))
all1=chosenword+chosennumber2+chosennumber
username="".join(all1)
print(username)


length = int(input('Enter the length of password: '))
print("password:")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num=string.digits
all2= lower+upper+num
temp= random.sample(all2, length)
password= "".join(temp)
print(password)
