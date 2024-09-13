import tkinter as tk
from tkinter import simpledialog

def is_even(n):
    return n % 2 == 0

ROOT = tk.Tk()
ROOT.withdraw()

USER_INP = simpledialog.askstring(title="홀짝 테스트기", prompt="숫자를 입력하세요:")

num = int(USER_INP)
if num == 0:
    print(f"{num}는(은) 0입니다.")
elif is_even(num):
    print(f"{num}는(은) 짝수입니다.")
else:
    print(f"{num}는(은) 홀수입니다.")
