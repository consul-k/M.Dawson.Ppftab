'''

Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его опадать. Компьютер
сообщает игроку, сколько букв в слове, и дает пяnь попыток узнать, есть ли какая-либо буква в слове, причем
программа может отвечаtь только «Да» и «Her». Вслед за тем игрок должен попробовать отгадать слово.

'''

import random

WORDS = ("питон", "город", "муравей", "паук", "ответ", "овсянка", "рынок")

word = random.choice(WORDS)
tries = 5
guess = ''

print(
"""
           Игра "Угадай загаданное компьютером слово"!
        
       У тебя есть 5 попыток узнать буквы скрытые в загаданном слове 
"""
)

print("В этом слове", len(word), "букв")


while tries != 0:
    guess = input("Есть ли тут буква - ")
    if len(guess)>1:
        print('Можно узнать только одну букву!')
    elif guess in word:
        print("Да!")
        tries -= 1
    elif guess not in word:
        print("Нет!")
        tries -= 1

print("Теперь назови слово: ")
guess = input()
if guess == word:
    print("Это оно! Вы угадали!\n")
else:
    print("Увы, вы проиграли\n")
