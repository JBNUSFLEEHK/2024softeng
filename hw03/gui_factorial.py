import tkinter as tk
from tkinter import simpledialog
from lec01.factorial import factorial

ROOT = tk.Tk()
ROOT.withdraw()

USER_INP = simpledialog.askstring(title="factorial", prompt="팩토리얼을 구하고 싶은 숫자를 입력하세요:")

num = int(USER_INP)
if num < 0:
    print("음수의 팩토리얼은 정의되지 않습니다.")
else:
    result = factorial(num)
    print(f"{num}! = {result}")
