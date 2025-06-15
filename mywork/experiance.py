# #args
# def sum_number(*numbers):
#     tota = 0
#     print("paramter type", type(numbers), end=" ")
#     for number in numbers:
#         tota += number
#         return tota
#
# a = sum_number(1, 2, 3, 4, 5)
# print(a)
#
#
# #**kwargs
# def function(**input):
#     for key, value in input.items():
#         print(f"type key {type(key)} and type value {type(value)}")
#         print(f"{key} = {value}")
#
# function(name= "udin dirgantara", umur= 23, alamat= "pekanbaru")
#
#
#
# #karna menggunakan loop sehingga bisa diakses
# def function(*input):
#     for asci in input:
#         print(f"type {type(asci)}")
#         print(f"this your input {asci}")
#
# function("udin", 2, "antot")
#
#
#
# #ditampilkan dalam bentuk tuple
# def function(*input):
#     print(f"type {type(input)}")
#     print(f"this your input {input}")
#
# function("udin", 2, "antot")

# print(dir())

# sys adalah library bawaan dari python/ standar library python
# import sys

# sys.argv menjalankan program dari terminal, contoh python3 <namaprogram> arif wahyu
# hasil kamu apa kabar arif
# nama saya : wahyu
# print("kamu apa kabar", sys.argv[1])
# print("Nama saya:", sys.argv[2])



# sys.exit berfungsi untuk keluar dari program ini
# sys.exit("bye bye")
# code ini tidak bisa dijalankan karena sys.exit
# print("Nama saya:", sys.argv[3])

# sys.stdin/stdout/stderr -> Saluran input/output/error

#library calender -> berfungsi untuk mendisplay dan memanipulasi calender
# import calendar

# first = calendar.firstweekday()
# print(type(first))

# print(calendar.month(2025, 6, 6))
# print(calendar.isleap(2020))
# #menghitung rentang tahun kabisat
# print(calendar.leapdays(2025, 2030))
# #menentukan hari dalam 1 minggu
# print(calendar.weekday(2025, 6, 10))

import time
import tkinter
from tkinter import Label

# tampil = tkinter.Tk()
# tampil.title("aplikasi timer")
# counter = tkinter.IntVar(value=0)
# lbl = tkinter.Label(tampil, textvariable=counter, font=("Helvetica", 32))
# lbl.pack(padx=210, pady=100)
#
# def timer():
#     counter.set(counter.get() + 1)
#     tampil.after(1000 , timer)
#
# timer()
# tampil.mainloop()

#timer sederhana
# second = int(input("masukan second yang you need "))

# while second >= 0:
#     print(second)
#     time.sleep(1)
#     second -= 1
#     if second == 0:
#         break

class Binatang:
    def suara(self):
        pass

class Kucing(Binatang):
    def suara(self):
        print("Meong~")

class Manager:
    pass

class Executive(Manager):
    pass

kucing = Kucing()
kucing.suara()

#isintance mengecek apa objek termasuk class tertentu
print(isinstance(kucing, Kucing))
print(isinstance(kucing, Manager))
#issubclass mengecek apakah class ini adalah subclass dari class lain
print(issubclass(Kucing, Binatang))
print(issubclass(Kucing, Manager))

class Minuman:
    def __init__(self):
        self.__rasa = "jeruk"
    def get_rasa(self):
        return self.__rasa
    def set_rasa(self, rasa_baru):
        self.__rasa = rasa_baru


m = Minuman()
print(m.get_rasa())
m.set_rasa("mangga")
print(m.get_rasa())