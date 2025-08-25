import sys
import time
from time import sleep

while True:
    a = int(input(f"введите число a: "))
    b = int(input(f"введите число b: "))
    
    deal = input(f"Выберите действие:\n1 - сложение\n2 - вычитание\nОтвет: ")
    if deal == "1":
        print(f"Сложив a и b получено: {a+b}")
    elif deal == "2":
        print(f"Вычив b из a получено: {a-b}")
    elif deal == "stop":
        sys.exit()
    else:
        print("Неверное значение")
    stop = input(f"Хотите завершить программу? (y/n): ")
    if stop == "y":
        print(f"Хорошо, завершаю работу!\n")
        sleep(1)
        sys.exit()
    if stop == "n":
        print(f"Хорошо, готов к работе!\n")