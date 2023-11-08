from datetime import datetime
from user import User
from colorama import Fore, Style

class TaskManager:
    username = ''

    def register_user(self, username_, password):  
        with open(f'{username_}.txt', 'a') as file:
            file.write(f"{username_},{password}\n")
            self.username = username_

    def login_user(self, username_, password):
        with open(f'{username_}.txt', 'r') as file:
            for line in file:
                user_info = line.strip().split(',')
                if user_info[0] == username_ and user_info[1] == password:
                    return User(username_, password)
        return "Username or password is incorrect. Try again!"
    
    def add_task(self, username, title, description, due_date):
        with open(f'{username}_tasks.txt', 'a') as file:
            file.write(f"{title},{description},{due_date}")

    def delete_task(self, username, task_index):
        with open(f'{username}_tasks.txt', 'r') as file:
            tasks = file.readlines()

        if len(tasks) == 0:
            print("Список задач пуст.")
            return

        with open(f'{username}_tasks.txt', 'w') as file:
            for i, task in enumerate(tasks):
                if i + 1 != task_index:
                    file.write(task)
                    
    def view_tasks(self, username): 
        with open(f'{username}_tasks.txt', 'r') as file: 
            tasks = file.readlines()

        if len(tasks) == 0:
            print("Список задач пуст")
        else:
            print(Style.NORMAL+ Fore.GREEN + "                                ✉︎  Список задач  ✉︎")
            for i, task in enumerate(tasks):
                details = task.split(",")
                title = details[0]
                description = details[1]
                due_date = details[2]
                
                print(Style.NORMAL+ Fore.LIGHTWHITE_EX +f"{i + 1}. Заголовок: {title}")
                print(Style.NORMAL+ Fore.LIGHTWHITE_EX +f"   Описание: {description}")
                print(Style.NORMAL+ Fore.LIGHTWHITE_EX +f"   Срок выполнения: {due_date}")
                print("")


    def sort_by_due_date(self):
        def get_due_date(task):
            return task.split(',')[2]

        tasks = []
        with open(f'{self.username}_tasks.txt', 'r') as file:
            tasks = [task.strip() for task in file.readlines()]
        tasks.sort(key=get_due_date)
        with open(f'{self.username}_tasks.txt', 'w') as file:
            for task in tasks:
                file.write(f'{task}\n')

    def get_today_tasks(self, filename):
        today_tasks = []
        today = datetime.today().strftime('%Y-%m-%d')
        with open(f'{filename}_tasks.txt', 'r') as file:
            for line in file:
                task_info = line.split(',')
                due_date = task_info[2].strip()
                if due_date == today:
                    today_tasks.append(line)
        return today_tasks
