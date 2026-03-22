import random
import platform
import os
def password():
    continuar = False
    correr_denuevo = False
    while correr_denuevo == False:
        while continuar == False:
            while True:
                try:
                    ask_length = int(input("Insert password length:\n"))
                    break
                except ValueError:
                    print("\n You have to input a number, try again\n")
            ask_uppercase = str(input("Use uppercase?: Y/n\n"))
            ask_lowercase = input("Use lowercase?: Y/n\n")
            ask_simbols = input("Use simbols?: Y/n\n")
            ask_numbers = input("Use numbers?: Y/n\n")
            letras = "abcdefghijklmnopqrstuvwyxz"
            simbolos = "!@#$%^&*()_+"
            numeros = "1234567890"
            opciones = ""
            contrasena_final = ""


            if ask_uppercase.lower() == "y":
                
                 ask_uppercase = "Yes"
                 opciones += letras.upper()
            else:
                ask_uppercase = "No"

            if ask_lowercase.lower() == "y":
                
                ask_lowercase = "Yes"
                opciones += letras
            
            else:
                ask_lowercase = "No"

            if ask_simbols.lower() == "y":
                ask_simbols = "Yes"
                opciones += simbolos
            
            else:
                ask_simbols = "No"
            
            if ask_numbers.lower() == "y":
                ask_numbers = "Yes"
                opciones += numeros 
            else:
                ask_numbers = "No"

            if opciones == "":
                input("Can't have an empty password! Enter to try again")
                
                os.system('clear' if platform.system() != 'Windows' else 'cls')
                continue
            
            os.system('clear' if platform.system() != 'Windows' else 'cls')
            continuar = input(f"\nYour password has {ask_length} caracteres.\n Caps?: {ask_uppercase}.\n Lowercase?: {ask_lowercase}.\n Simbols?: {ask_simbols}.\n Numbers? {ask_numbers}.\n\n  Continue?: Y/n ")

            
            
            if continuar.lower() == "y":
                continuar = True
                os.system('cls')

                for _ in range(ask_length):
                    caracteres_random = random.choice(opciones)
                    contrasena_final += caracteres_random
            
                print(contrasena_final) 

            else: 
                continuar = False
                os.system('clear' if platform.system() != 'Windows' else 'cls')
                continue
                

            correr_denuevo = input("Generate another password?: Y/n\n")

            if correr_denuevo.lower() == "y":
                os.system('clear' if platform.system() != 'Windows' else 'cls')
                correr_denuevo = False 
                continuar = False

            else:
                correr_denuevo = True
                os.system('clear' if platform.system() != 'Windows' else 'cls')
                
            

    
password()

input("\n\nPresiona Enter para salir")

