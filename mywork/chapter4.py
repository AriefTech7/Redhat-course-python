#exercise 4.1
# def validate(masukk):
#     if masukk > 0 :
#         return masukk
#     else:
#         return 0
#
# try:
#     nomor = int(input("give me positive integer to validate "))
#
#     hasil = validate(nomor)
#
#     if hasil == 0:
#         print(f"invalid {nomor}")
#     else:
#         print(f"valid {nomor}")
# except ValueError:
#     print("your input not a integer")



#exercis 4.2

#def panjang(name):
#     return len(max(name))
#
# words = ["hello", "supercalafragalistic", "Q", "moose", "functions!"]
# hasil = panjang(words)
#
# for word in words:
#     print(f"{word:^{hasil}}")

#exercise 4.3

# def jumlah(angka):
#     jumlahnya = 0
#     for i in angka:
#         jumlahnya += i
#     return jumlahnya
#
# nomor = [9, 8, 7]
# print(jumlah(nomor))
# nomor2 = [17, 10, 3, 5, 1, 6]
# print(jumlah(nomor2))
#
# nomor3 = [10, 19]
# print(f"jumlah dari 10 ditambah 19 = {jumlah(nomor3)}")

#exercise 4.4
# def jumlah_and_rata(*angka):
#     jumlahnya = 0
#     for i in angka:
#         jumlahnya += i
#     rata = jumlahnya / len(angka)
#     return (f"{jumlahnya} and average {rata}")
#
#
# print(f"ini adalah rata dan penjumlahan dari 9, 8, 7 = jumlah {jumlah_and_rata(9,8,7)}")
# nomor = (9,8,7) # jika kamu menggunakan variabel tuple disaat kamu menggunakan *args yang bertipe tuple akan menjadi error
# print(jumlah_and_rata(nomor))

#exercise 4.5
# def kalkulator():
#     while True:
#         tampilan_kalkulator = {
#             1:"add",
#             2:"Subtract",
#             3:"Multiply",
#             4:"Divide",
#             5:"Quit"
#         }
#
#         print("Calculator options:")
#         for x, y in tampilan_kalkulator.items():
#             print(f"\t{x}.{y}")
#
#         key = list(tampilan_kalkulator.keys())
#         # choce = input("choce action/operation ").capitalize()
#         choce = (int(input("choce action/operation ")))
#         if choce == key[4]:
#             print("Exiting...")
#             break
#
#         once_number = int(input("enter a number "))
#         twice_number = int(input("enter an number "))
#
#
#         if choce == key[0]:
#             hasil1 = once_number + twice_number
#             print(f"{once_number} + {twice_number} = {hasil1}")
#         elif choce == key[1]:
#             hasil2 = once_number - twice_number
#             print(f"{once_number} - {twice_number} = {hasil2}")
#         elif choce == key[2]:
#             hasil3 = once_number * twice_number
#             print(f"{once_number} * {twice_number} = {hasil3}")
#         elif choce == key[3]:
#             hasil4 = once_number / twice_number
#             print(f"{once_number} / {twice_number} = {hasil4}")


# kalkulator()

#exercise 4.6

# data_bersih = []
# def filterisasi(*angka):
#     for angka_tunggal in angka:
#         if angka_tunggal > 0:
#             data_bersih.append(angka_tunggal)
#
#     return data_bersih
#
#
# print(filterisasi(-3, 5, 0, 8, -1))

#exercise 4.7
# def function(*banyak, number):
#     result = 0
#     for elem in banyak:
#         if elem > number:
#             result += 1
#     return result
#
# limit = 10
# h = function(5, -10, 10, -20, 30, number=limit)
# print(h)

#exercise 4.8
# def luar(a, b):
#     def dalam():
#         hasil = a + b
#     # return dalam() berfungsi untuk mengembalikan ke function dalam() dan langsung dijalankan
#         return hasil
#     return dalam()
#
#
# print(luar(10 ,2 ))

#exercise 4.9
# def luar():
#     def dalam(a, b):
#         hasil = a + b
#         print(f"hasil {a} ditambah {b} adalah {hasil}")
#     # return dalam berfungsi untuk mengembalikan ke function dalam() tetapi tidak dijalakan
#     return dalam
#
#
# rumus = luar() # ini adalh metode untuk menggunakannya
# rumus(10, 2)

#exercise 4.10
# def luar():
#     hasil = lambda a, b : a + b
#     return hasil
#
# rumus = luar()
# print(f"ini adalah hasil penjumlahannya {rumus(10, 9)}")

#exercise 4.11
# def take_list(list1, list2):
#     v1 = set(list1)
#     v2 = set(list2)
#     collect = v1 & v2
#     return list(collect)
#
# a = [80, 70, 60, 50, 40, 30]
# b = [10, 40, 30, 20, 5]
# print(take_list(a, b))

#exercise 4.12
# numbers = {'a': 1, 'b': 2, 'c': 3}
# def add_dict(*number):
#     num_list = list(number)
#     numbers["a"] = num_list[0]
#     numbers["b"] = num_list[1]
#     numbers["c"] = num_list[2]
#     return numbers
#
# print(add_dict(10, 20, 30))
# print(add_dict(40,50,60))

# def add_dict_2(the_dict, number):
#     for element in the_dict:
#         the_dict[element] = the_dict[element] + number
#
#
# item = {'a': 1, 'b': 2, 'c': 3}
# print(item)
# add_dict_2(item, 10)
# print(item)

#exercise 4.13
#masih ga ngerti flowcode ini
# try:
#     def search_list(data, obejct, dimana):
#         start = 0
#         for x in range(dimana):
#             found_me = data.index(obejct, start)
#             start = found_me + 1
#         return found_me
#
#     data = ['a', 'b', 'a', 'c', 'a']
#     temukan_saya = "a"
#
#     for offset in range(1, 5):
#         print(f"Occurrence {offset} of {temukan_saya} is at",
#               search_list(data, temukan_saya, offset))
# except UnboundLocalError and ValueError:
#     if ValueError:
#         print("'a' is not in list")
#     elif UnboundLocalError:
#         print("cannot access local variable 'found_me' where it is not associated with a value")


def sapa():
    return "hello"
ucap = sapa()
print(ucap)