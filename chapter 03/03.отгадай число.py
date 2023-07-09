import random  

print("\tДобро пожаловать в 'Отгадай число'!")
print("\nЯ думаю о числе между 1 и 100...")
print("Постарайтесь отгадать его за 7 попыток.\n")


the_number = random.randint(1, 100)
tries = 0
guess = 0

while guess != the_number and tries < 7:
    guess = int(input("Ваша догадка: "))
    if guess > the_number:
        print("Меньше...")
    else:
        print("Больше...")
    tries += 1
    
if guess == the_number:
    print("Вы угадали! Это число было", the_number)
    print("И это стоило всего", tries, "попыток!\n")
else:
    print("Ты проиграл компьютеру, кожанный мешок! И это стоило тебе", tries, "попыток!")
  
input("\n\nНажмите Enter, чтобы выйти.")
