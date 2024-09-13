import tkinter as tk
from tkinter import simpledialog
from lec01.prime_number import is_prime

ROOT = tk.Tk()
ROOT.withdraw()

USER_INP = simpledialog.askstring(title="prime number list", prompt="숫자를 입력하세요:")

num = int(USER_INP)
primes = []
for i in range(2, num):
    if is_prime(i):
        primes.append(i)
print(primes)
