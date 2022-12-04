import os


def function():
    oi = input("Хотите создать Папку?")
    trj = "Да"
    urh = "Нет"
    if oi == trj:
        ash = input("Напишите Название Папки:")
        jkasu = input("Введите название места на диске куда поместить папку")
        os.makedirs(f"{jkasu}{ash}")

print("Здравствуйте! Для запуска аккаунта администратора вам нужно ввести пароль и логин.")
answer = input("Логин:")
answer2 = int(input("Пароль:"))
axll = "Axol"
if answer == axll:
    print("Доступ Разрешен")
if answer2 == 205465:
     function()
