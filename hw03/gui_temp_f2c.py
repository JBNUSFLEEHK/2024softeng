import tkinter as tk
from tkinter import simpledialog


def f2c(temp_f: float) -> float:  
    return (temp_f-32)*5/9


ROOT = tk.Tk()
ROOT.withdraw()

USER_INP = simpledialog.askstring(title="f2c", prompt="화씨 온도를 입력하세요:")

typed_temp_f = int(USER_INP)
temp_c = f2c(typed_temp_f)
print(f"{typed_temp_f}F => {temp_c:.1f}C")

