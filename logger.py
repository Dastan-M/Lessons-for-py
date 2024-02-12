from data_create import input_user_data


def input_data():
    name, surname, phone, adress = input_user_data()
    var = int(input(f'\nВ каком формате записать данные? \n'
                    f'1 Вариант:\n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант:\n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write( f'{name}\n'
                        f'{surname}\n'
                        f'{phone}\n'
                        f'{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')


def print_data():
    print('1 файл:')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))
        
    print('2 файл:')
    with open('data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        print(''.join(data))

import shutil

def copy_data(data_number=None):    
    var = int(input('Скопировать откуда? \n'
                    '1 - Скопировать из 1 файла во 2 \n'
                    '2 - Скопировать из 2 файла в 1 \n'
                    'Ваш выбор: '))
    if var == 1:
        with open('data_first_variant.csv', 'r') as source:
            lines = source.readlines()

            if data_number is None:
                data_number = int(input("Введите номер данных для копирования: "))

            if 1 <= data_number <= len(lines):
                data_to_copy = lines[data_number - 1]

                with open('data_second_variant.csv', 'a') as destination:
                    destination.write(data_to_copy)
                
                print(f"Данные успешно скопированы в {'data_second_variant.csv'}")
    else:
        with open('data_second_variant.csv', 'r') as source:
            lines = source.readlines()

            if data_number is None:
                data_number = int(input("Введите номер данных для копирования: "))

            if 1 <= data_number <= len(lines):
                data_to_copy = lines[data_number - 1]

                with open('data_first_variant.csv', 'a') as destination:
                    destination.write(data_to_copy)
                
                print(f"Данные успешно скопированы в {'data_first_variant.csv'}")   
            else:
                print("Некорректный номер данных. Пожалуйста, введите правильное значение.")
 

