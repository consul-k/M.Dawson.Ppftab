'''

Напишите программу «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
30 пунктов, которые можно распределить между четырьмя характеристиками: Сипа, Здоровье, Мудрость
и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пула», 
но и возвращать их туда из характеристик, которым он решит присвоить другие значения.

'''

print("\t\t\tГенератор персонажей для ролевой игры\n")

# персонажи
chars = {}

 # Пример
 # chars = {"id1': {'name':'leon', 'power':12, 'health':7 , 'wisdom':5, 'dex-ty':6 }}

# меню выбора
def menu():

    choice = None

    while choice != '0':
        print(
        """

        Управление программой:
        0 - Выйти
        1 - Добавить нового персонажа
        2 - Перераспределить характеристики персонажа
        3 - Показать созданных персонажей
        4 - Удалить персонажа

        """
        )
        
        choice = input("Ваш выбор: ")
        
        if choice == '0':
            print("До свидания")
        elif choice == '1':
            create()
        elif choice == '2':
            red_points()
        elif choice == '3':
            show()
        elif choice == '4':
            delete()
        else:
            print('Ошибка ввода!')

#создание персонажа
def create():

    #создание id персонажа
    identifier = 'id' + str(len(chars))
    chars[identifier] = {}
   
    #характеристики
    stats = {'name':0,'power':0,'health':0,'wisdom':0,'dex-ty':0}

    #создание имени
    name = input('Введите имя персонажа: ')
    stats['name'] = name

    #добавить значения характеристик
    def add_stats():
        
        #количество очков для распределения
        pool = 30
        
        for stat in stats:
            if stat == 'name':
                continue

            print(stat, end=' ')

            if pool == 0:
                print('0 - у вас закончились очки для распределения!')
                n = 0
            else:
                try:
                    n = int(input())
                    if n < 0:
                        print('Только положительные числа')
                    elif (pool - n) < 0:
                        print('Слишком много!')
                    else:
                        pool -= n
                except ValueError:
                    print('Можно вводить только числа')
                stats[stat] = n

        if pool > 0:
            print('У вас осталось неиспользовано ', pool, 'очков')
            ask = None
            while ask != 'Y' and ask != 'N':
                ask = input('Хотите добавить их? (Y|N) ').upper()
            if ask == 'Y':
                add_stats()

    add_stats()

    chars[identifier] = stats


#редактирование персонажа
def red_points():
    identifier = None
    pool = 30
    
    #проверка, есть ли id в словаре персонажей
    while identifier not in chars:
        identifier = input('Выберите id персонажа, которого вы хотите изменить: ')
        if identifier not in chars:
            print('ID отсутствует!')

    #проверяем сколько осталось неиспользованных очков
    for stats in chars[identifier]:
        if stats != 'name':
            pool -= chars[identifier][stats]
        print(stats, chars[identifier][stats])
    
    print('У вас осталось ', pool,' неиспользованых очков' )
    
    #свободные очки
    free_scores = pool

    #переменная переключатель
    ending = None

    #цикл изменения характеристик
    while ending != 'N':

        #если свободных очков не осталось
        if free_scores == 0:
            print('У вас не хватает свободных очков! Вы можете сбросить характеристики, чтобы получить свободные очки')
            ask = None
            while ask != 'Y' and ask != 'N':
                ask = input('Выполнить полный сброс текущих хар-к? Все значения станут 0 (Y|N) ').upper()
            if ask == 'Y':
                free_scores = 30
                for stats in chars[identifier]:
                    if stats != 'name':
                        chars[identifier][stats] = 0
            else:
                break
                
        #если есть свободные очки
        elif free_scores > 0:

            stat = input('Выберите характеристику, которую вы хотите изменить: ')
            while stat not in chars[identifier]:
                    stat = input('Данной характеристики не существует! Выберите характеристику, которую вы хотите изменить: ')

            if stat == 'name':
                print(chars[identifier][stat], end=' ')
                chars[identifier][stat] = input()
            else:
                #новое значение хар-ки
                new_stat_value = None
                #проверка допустимости введенного значения
                perm_value = None
                
                while perm_value != True:
                    
                    try:
                        print(stat, end=' ')
                        new_stat_value = int(input())

                        if new_stat_value  < 0:
                            print('Только положительные числа')
                        
                        elif (free_scores - new_stat_value) < 0:  
                            print('Вы хотите добавить слишком много! У вас ', free_scores, ' очков')
                        else:
                            perm_value = True

                    except ValueError:
                        print('Можно вводить только числа')

                if chars[identifier][stat] < new_stat_value:
                    chars[identifier][stat] += new_stat_value
                    free_scores -= new_stat_value
                elif chars[identifier][stat] > new_stat_value:
                    chars[identifier][stat] -= new_stat_value
                    free_scores += new_stat_value

                print('У вас осталось', free_scores, 'свободных очков')


        while ending != 'N' and ending != 'Y':
            ending = input('Вы хотите продолжить редактирование? (Y|N) ').upper()

# показ созданных персонажей
def show():
    if len(chars) == 0:
        print('Нет созданных персонажей')
    for identifier in chars:
        print(identifier)
        for sets in chars[identifier]:
            print(sets, chars[identifier][sets])

# удаление персонажа
def delete():
    delete = input('Введите ID персонажа, которого вы хотите удалить: ')   
    if delete in chars:
        del chars[delete]
    else:
        print('ID отсутствует, либо неверный ввод!')


menu()
input('\n\nНажмите Enter, чтобы выйти')
