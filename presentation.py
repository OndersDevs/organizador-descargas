print("Hola buenos dias.")
print('Por favor ingrese su nombre completo.')
name = input('> ')
print('Ahora su edad actual.')
edad = input('> ')
print('Su ciudad de residencia.')
ciudad = input('> ')

print(f'Hola, {name.capitalize()}. Tienes {edad} años y vives en {ciudad.capitalize()}. En 2027 tendrás {int(edad) + 1} años.')