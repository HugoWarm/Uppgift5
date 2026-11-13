import os
import subprocess
import random
import time
subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)



# while True:
#     text=input("Skriv någonting med bara siffror ")
#     if text.isdigit() == True:
#         break
#     else:
#         print("Skriv inte något annat än siffror\n")

# print("Bra att du kan följa instruktioner")

# word=input("skriv ett ord så skriver jag ut de tre första bokstäverna av ordet ")

# print(word[:3])

# idk="ord"
# if len(idk)>5:
#     print(idk[:5]+"...")
# else:
#     print(idk)

# test="ABBE"
# if len(test)<5:
#     print(test.lower())
# else:
#     print(test.upper())

# while True:
#     num1=random.randint(1,13)
#     points=0
    
#     while True:
#         subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
        
#         num2=random.randint(1,13)
        
        
#         print("Det första talet är",num1,"\n")

#         answer=input("Kommer nästa tal vara högre eller lägre?\nH = Högre L = Lägre Q om du vill avsluta")
#         time.sleep(0.2)
#         print("\nDet andra talet va",num2)

#         if answer.upper()=="H" and num1<=num2:
#             print("Korrekt")
#             time.sleep(0.5)
#             points+=1
#             print("Du har",points,"poäng\n")
#             time.sleep(0.5)
#         elif answer.upper()=="L" and num1>=num2:
#             print("Korrekt")
#             time.sleep(0.5)
#             points+=1
#             print("Du har",points,"poäng\n")
#             time.sleep(0.5)
#         elif answer.upper()=="Q":
#             exit()
#         else:
#             print("Fel")
#             time.sleep(0.1)
#             break
#         num1=num2
#     print("Du fick",points,"poäng")
#     resatrt=input("Vill du köra igen?\nN = Nej ")
#     if resatrt.upper()=="N":
#         exit()



