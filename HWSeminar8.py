
from pathlib import Path
file_data = Path("phone_book.txt")

def add_person():
    last_name = input('Введите фамилию: ')
    name = input('Введите имя: ') 
    surname = input('Введите отчество: ') 
    phone = input('Введите номер телефона: ') 
    data = open('phone_book.txt', 'a', encoding='UTF-8')
    data.write(f'{last_name} {name} {surname} {phone}\n')
    data.close()

def print_data():
    with open('phone_book.txt', 'r', encoding='UTF-8') as data:
        
            print(data.read())

def search():
    search_name = input('Введите данные для поиска: ')
    with open('phone_book.txt', 'r', encoding='UTF-8') as data:
        for line in data:
            if search_name in line:
                print(line)


def del_person():
    del_name = input('Введите Фамилию, который нужно удалить: ')
    with open('phone_book.txt', 'r', encoding='UTF-8') as data:
        d = data.readlines()
        for i_line in range(len(d)):
            if del_name in d[i_line]:
                del d[i_line]
    with open('phone_book.txt', 'w', encoding='UTF-8') as data:
        for line in d:
            data.write(line)
            
def change_person():
    change_name = input('Введите данные контакта, который хотите изменить: ')
    last_name = input('Введите новую фамилию: ') 
    name = input('Введите новое имя: ') 
    surname = input('Введите новое отчество: ') 
    phone = input('Введите новый номер телефона: ')
    
    with open('phone_book.txt', 'r', encoding='UTF-8') as data:
        d = data.readlines()
    for i_line in range(len(d)):
        if change_name in d[i_line]:
            d[i_line] = (f'{last_name} {name} {surname} {phone}\n')
    
    with open('phone_book.txt', 'w', encoding='UTF-8') as data:
        for line in d:
            data.write(line)

def main():
    
    flag = True
    while flag:
        print('0 - Выход')
        print('1 - Добавить контакт')
        print('2 - Поиск')
        print('3 - Показать контакты')
        print('4 - Удалить контакт')
        print('5 - Изменить контакт')
     
        user_input = input('Введите действие: ')
        if user_input == '0':
            flag = False
        elif user_input == '1':
            add_person()
        elif user_input == '2':
            search()                 
        elif user_input == '3':
            print_data()
        elif user_input == '4':
            del_person()
        elif user_input == '5':
            change_person()
    


    
if __name__ == "__main__":
    main() 

  