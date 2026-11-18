print(f"Exponenciación 2 elevado a 4 = {2**4}")
print(f"Módulo o resto 22 % 8 = {22 % 8}")
print("División de enteros 22 // 8 = " + str(22 // 8))
print("División 22 / 8 = " + str(22 / 8))
print("Y el resto ya te lo sabes.")

#Estudio de los flujos del codigo.
"""spam = 4
print(2 + 2 == spam and not 2 + 2 == (spam + 1) and 2 * 2 == 2 + 2)
print(f'{spam}')

username = 'Onder'
password = 'swordfish'
if username == 'Onder':
    print(f'Hello, {username}')
    if password == 'swordfish':
        print("Acces granted.")
    else:
        print('Wrong password.')

age = 2
if username == 'Onder2':
    print(f'Hi, {username}  {age > 12}')
elif age < 12:
    print("You are not Onder, kiddo.")


name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are neither Alice nor a little kid.')"""

today_is_opposite_day = False

# Set say_it_is_opposite_day based on today_is_opposite_day:
if today_is_opposite_day == True:
    say_it_is_opposite_day = True
else:
    say_it_is_opposite_day = False

# If it is opposite day, toggle say_it_is_opposite_day:
if today_is_opposite_day == True:
   say_it_is_opposite_day = not say_it_is_opposite_day

# Say what day it is:
if say_it_is_opposite_day == True:
    print('Today is Opposite Day.')
else:
    print('Today is not Opposite Day.')