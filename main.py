from user import User
from helper_modules import TaskManager
from colorama import Fore, Style
task_manager = TaskManager()

print (Style.NORMAL+ Fore.GREEN +"                      Планер задач: уверенный шаг к успеху через эффективное планирование") 
print (Style.NORMAL+ Fore.LIGHTWHITE_EX +"🔷🔹 1) Регистрация") 
print(Style.NORMAL+ Fore.LIGHTWHITE_EX +"🔷🔹 2) Войти")
print(Style.NORMAL+ Fore.LIGHTRED_EX +"🔷🔹 0) Выход")

run = True

while run:
   
    number = input(Style.NORMAL+ Fore.LIGHTBLUE_EX +"✍  Что вас интересует? ")

    if number == '1':
        print(Style.NORMAL+ Fore.WHITE +"Регистрация пользователя")
        username = input(Style.NORMAL+ Fore.CYAN +"Имя пользователя: ")
        password = input(Style.NORMAL+ Fore.CYAN +"Пароль: ")
        task_manager.register_user(username, password)

    elif number == '2':
        print(Style.NORMAL+ Fore.GREEN +"                 ⚡ Вход в систему")
        username = input(Style.NORMAL+ Fore.CYAN +"Имя пользователя: ")
        password = input(Style.NORMAL+ Fore.CYAN +"Пароль: ")
        user = task_manager.login_user(username, password)
        if isinstance(user, User):

            print(Style.NORMAL+ Fore.GREEN +"                 ✅ Вход успешен             ")
            print(Style.NORMAL+ Fore.WHITE +"🔷🔹 3) Добавить задачу                        ")
            print(Style.NORMAL+ Fore.WHITE +"🔷🔹 4) Сортировать задачи по сроку выполнения ")
            print(Style.NORMAL+ Fore.WHITE +"🔷🔹 5) Задачи на сегодня                      ")
            print(Style.NORMAL+ Fore.WHITE +"🔷🔹 6) Удалить задачу                         ")
            print(Style.BRIGHT+ Fore.LIGHTRED_EX +"🔷🔹 0) Выход                                  ")
        else:
            print(Style.NORMAL+ Fore.RED +"⚠️ Неправильное имя пользователя или пароль")

    elif number == '3':
        print(Style.NORMAL+ Fore.GREEN +                  "⚡ Добавление задачи")
        if user:
            task = input(Style.NORMAL+ Fore.WHITE +"Задача: ")
            description = input(Style.NORMAL+ Fore.WHITE +"Описание: ")
            date = input(Style.NORMAL+ Fore.WHITE +"Дата (ГГГГ-ММ-ДД): ")
            task_manager.add_task(user.username, task, description, date)


    elif number == '4':
        print(Style.BRIGHT+ Fore.GREEN +               "⚡ Сортировка задач по сроку выполнения")
        with open(f'{user.username}_tasks.txt', 'r') as file:
            sorted_tasks = file.readlines()
        for task in sorted_tasks:
            print(task)

    elif number == '5':
        print("⚡ Задачи на сегодня")
        today_tasks = task_manager.get_today_tasks(user.username)
        for task in today_tasks:
            print(task)
       
    elif number == '6':
        task_manager.view_tasks(user.username)
        task_index = int(input(Style.NORMAL+ Fore.WHITE +"Введите индекс задачи, которую хотите удалить: "))
        task_manager.delete_task(user.username, task_index)

    elif number == '0':
        run = False
