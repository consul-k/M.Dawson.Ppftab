'''

Напишите программу «Кто твой папа?», в которой пользователь будет вводить имя человека, а программа - 
называть отца этого человека. Чтобы было интереснее, можно «научить» программу родственным
отношениям среди литературных персонажей, исторических лиц и современных знаменитостей. Предоставьте
пользователю возможность добавлять, заменять и удалять пары «СЫН - отец».

'''

son_dad = {'Tirion' : 'Taiwin','Aria' : 'Ned Star','Jon' : 'Raegar',
           'Jendry' : 'Robert'}

choice = None

while choice != "0":
    print(
    """
    Управление программой:
    0 - Выйти
    1 - Найти отца персонажа
    2 - Добавить пару
    3 - Изменить отца
    4 - Удалить пару
    """
    )
    choice = input("Ваш выбор: ")

    print()     #?
    if choice == "0":
        print("До свидания")
    elif choice == "1":
        son = input("Чей отец вам интересен? ")
        if son in son_dad:
            father = son_dad[son]
            print("\n", son,"имеет отца",father)
        else:
            print("\nУвы, нет данных о: ", son)
    elif choice == "2":
        son = input("Какого отпрыска вы хотите добавить? ")
        if son not in son_dad:
            father = input("\nВведите отца: ")
            son_dad[son] = father
            print("\nГерой", son, "добавлен в словарь.")
        else:
            print("\nТакой герой уже есть!")
    elif choice == "3":
        son = input("Чьего отца вы хотите изменить? ")
        if son in son_dad:
            father = input("Введите нового отца: ")
            son_dad[son] = father
            print("\nГерой", son, "получил исправленную версию!")
        else:
            print("\nТакого героя у нас нет!")
    elif choice == "4":
        son = input("Какого героя вы хотите удалить? ")
        if son in son_dad:
            del son_dad[son]
            print("\nГерой", son, "удален.")
        else:
            print("\nНичем не могу помочь. Героя ",son,"нет в словаре")

    else:
        print("В меня нет такого пункта", choice)
        
    input("\n\nНажмите Enter, чтобы выйти.")
