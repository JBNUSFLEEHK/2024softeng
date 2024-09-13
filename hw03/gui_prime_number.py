import tkinter as tk
from tkinter import simpledialog

def is_prime(n: int) -> bool:
    if n < 2:
        return False

    for i in range(2,n):
        if n % i == 0:
            return False

    return True

ROOT = tk.Tk()
ROOT.withdraw()

USER_INP = simpledialog.askstring(title="prime number", prompt="숫자를 입력하세요:")

num = int(USER_INP)
if is_prime(num):
    print(f"{num}는(은) 소수입니다.")

else:
    print(f"{num}는(은) 소수가 아닙니다.")
