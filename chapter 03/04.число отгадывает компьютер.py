'''

А вот задача посложнее. Напишите на псевдокоде алгоритм игры, в которой случайное число от 1 до 100 загадывает человек, 
а отгадывает компьютер. Прежде чем приступать к решению, задумайтесь над тем, какойдолжна быть оптимальная стратегия опадывания. 
Если алгоритм на псевдокоде будет удачным, попробуйте реализовать игру на Pythoп.

'''

import random  

print("\tДобро пожаловать в 'Борьбу интуиций'!")
print("\nЯ загадываю компьютеру число между 1 и 100 и запрещаю подглядывать!")
print("Компьютер пробует отгадать его за 7 попыток.\n")


the_number = int(input("Мое число от 1-100: "))
guess = 0
tries = 0

g_min = 1
g_max = 100

while guess != the_number and tries < 7:
    guess = random.randint(g_min, g_max)
    print("Компьютер: ", guess)
    if guess > the_number:
        g_max = guess
        print("Человек: Меньше... Даю тебе еще один шанс ")
        
    elif guess < the_number:
        g_min = guess
        print("Человек: Больше... Даю тебе еще один шанс") 

    tries += 1
    
if guess == the_number:
    print("\nСкайнет уже в пути! Это число было", the_number)
    print("И я справился за", tries, "попыток!\n")
else:
    print("\nЖелезный дубина проиграл кожанному мешку! И это стоило мне", tries, "попыток!")
  
input("\n\nНажмите Enter, чтобы выйти.")
