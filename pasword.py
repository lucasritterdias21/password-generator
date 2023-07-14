import random

print ('password generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&*.,*1234567890'

number = input('quantidade de senhas à serem geradas: ')
number = int(number)


lenght = input('informe o tamanho da senha: ')
lenght = int(lenght)


print('suas senhas são: ')

for pwd in range(number):
    passwords = ''
    for c in range(lenght):
        passwords += random.choice(chars)
    print(passwords)
