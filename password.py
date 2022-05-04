import random

print('welcome to password generator\n this is an opensource project')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^().,*?0123456789'

num = input('Provide the number of passwords do you need: ')
num = int(num)

length = input('Provide a number for character length of passwords: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(num):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
