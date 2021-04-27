import tkinter as tk
from functools import partial
import os
import sys


def restart_program():
   number1.set("")
   number2.set("")


def romantoint(rom):
    if not rom:
        return 0
    roman = dict({'I': 1, 'V': 5, 'X': 10 , 'L': 50, 'C': 100, 'D': 500, 'M':1000})
    i = 0
    n = len(rom)
    result = 0
    while i < n-1:
        result += (-roman[rom[i]]) if roman[rom[i+1]] > roman[rom[i]] else (roman[rom[i]])
        i += 1

    result += roman[rom[n-1]]
    return result

def inttoRoman(num):
    values = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'DM', 'M']
    i = len(values) - 1
    result = ''
    while i >= 0 and num > 0:
        count = num / values[i]
        #print(count)
        while count >= 1:
            result += roman[i]
            #print(result)
            count -= 1
            num -= values[i]
        i -= 1
    return result

def call_result(label_result, n1, n2):
    if len(n1.get()) == 0:
        num2 = str(n2.get())
        label_result.config(text="Result is %d" % romantoint(num2))
    else:
        num1 = int(n1.get())
        label_result.config(text="Result is %s" % inttoRoman(num1))
    # num1 = (n1.get())
    # num2 = (n2.get())
    # result = int(num1) + int(num2)
    # label_result.config(text="Result is %d" % result)
    return



root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Roman <-> Integer')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelTitle = tk.Label(root, text="Roman to Integer").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter an Integer").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Enter a Roman number").grid(row=2, column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)
button_Reset = tk.Button(root, text="Reset Values", command=restart_program).grid(row =4, column =0)
root.mainloop()
