from string import ascii_lowercase
import getpass

contador=0

password=getpass.getpass("ingrese la contraseña: ").lower()
print(password)

abc=ascii_lowercase

for letra in password:
    for caracter in abc:
        contador+=1
        if letra ==caracter:
            break
print(f"la contraseña fue forzada en  {contador} iteraciones y la contraseña es {password}")
        