# def cek_umur(umur):
#     if umur < 0:
#         raise ValueError("Umur tidak boleh negatif!")
#     print("Umur valid:", umur)
#
# try:
#     cek_umur(10)
# except ValueError as l:
#     print("Terjadi kesalahan:", l)

# def main():
#     total = 0
#     pesanan = "silahkan masukkan angka atau ketik 'end' untuk keluar "
#
#     while True:
#         try:
#             nilai = input(pesanan).lower()
#             if nilai == "end":
#                 break
#             total += int(nilai)
#         except ValueError:
#             print("input tidak valid")
#         except EOFError:
#             print("input diberhentikan. segera keluar")
#             break
#
#     print(f"total pesanan", total)
#
# if __name__ == "__main__":
#     main()

#exercise 7.1

# a = [1,2,3,4,5,6,7,8,9,10]
#
# class IndexOutRange(Exception):
#     pass
#
#
# try:
#     user = input("enter a number and type 'end' out from this program ")
#     if user.lower() == "end":
#         print("program berhenti")
#     else:
#         try:
#             user = int(user)
#         except ValueError:
#             raise ValueError("your input not valid, please input integer")
#         for index, angka in enumerate(a):
#             if user == angka:
#                 print(f"ini angka {angka} dan ini indexnya {index}")
#
#         if user > max(a):
#             raise IndexOutRange("your input out from integer")
#
#
#
# except ValueError as e:
#     print("terjadi kesalahan:", e)
#
# except IndexOutRange as i:
#     print("terjadi kesalahan:", i)

#exercise 7.2

# a = [1,2,3,4,5,6,7,8,9,10]
#
# class IndexOutRange(Exception):
#     pass
# class NegativeNumber(Exception):
#     pass
#
# try:
#     user = input("enter a number and type 'end' out from this program ")
#     if user.lower() == "end":
#         print("program berhenti")
#     else:
#         try:
#             user = int(user)
#         except ValueError:
#             raise ValueError("your input not valid, please input integer")
#         for index, angka in enumerate(a):
#             if user == angka:
#                 print(f"ini angka {angka} dan ini indexnya {index}")
#
#         if user > max(a):
#             raise IndexOutRange("your input out from integer")
#         if user < 0:
#             raise NegativeNumber("your input is negative, please try again")
#
#
# except NegativeNumber as y:
#     print("terjadi kesalahan:", y)
#
# except ValueError as e:
#     print("terjadi kesalahan:", e)
#
# except IndexOutRange as i:
#     print("terjadi kesalahan:", i)

#exercise 7.3

data = 0
try:
    while True:
        user = input("give me a integer ")
        if user == "end":
            print("program berhenti")
            break

        else:
            user_integer = int(user)
            if user_integer > 0:
                data += user_integer

    print(data)

except ValueError:
    print("terjadi mistakes: Pleasa try again")

except KeyboardInterrupt:
    print(" terjadi mistakes: control-c untuk langsung keluar")

except EOFError:
    print("keluar dari loop")
    print(f"sum of all data {data}")