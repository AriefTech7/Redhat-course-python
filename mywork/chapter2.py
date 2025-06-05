#exercise 2.1
# lucky = input("enter your luck number: ")
# try:
#     number_lucky = int(lucky)
#     print(f" your lucky number is {number_lucky}")
# except ValueError:
#     print("That's not a valid integer. Please enter a whole number.")

#exercise 2.2
# lucky = input("enter your luck number: ")
# try:
#     number_lucky = int(lucky)
#     print(f" your lucky number is {number_lucky} has {len(lucky)} digit(s)")
# except ValueError:
#     print("That's not a valid integer. Please enter a whole number in integer.")

#exercise 2.3
# once = int(input("enter a number integer: "))
# twice = int(input("enter an number integer: "))
#
# if once > twice:
#     print(f"{once} is the larger number")
# elif twice > once:
#     print(f"{twice} is the larger number")
# elif once == twice:
#     print("The numbers are equal")

#exercise 2.4
# pertama = int(input("enter a number integer: "))
# kedua = int(input("enter a number integer: ")) + 1
# print()
# print(f"sum for {pertama} to {kedua - 1}")
#
# a = sum(range(pertama, kedua))
# print(f"this is a result {a}")

#exercise 2.5
# num = input("enter multiple number here: ")
# x = num.split()

# for nomor in x:
#     nomor = int(nomor)
#     if nomor > 0:
#         print(nomor, end=" ")

#exercise 2.6
# lower_limit = int(input("enter number lower limit: "))
# higher_limit = int(input("enter number higher limit: "))
# step = int(input("enter number multiples: "))

# for num in range(lower_limit, higher_limit, step):
#     print(num)

#exercise 2.7
# for number in range(0, 50):
#     print(number, end=" ")
#     if number <= 9:
#         print(end=" ")
#     if number % 10 == 9:
#         print(end="\n")

#exercise 2.8
# prompt = "Enter {} integer: "
# first = int(input(prompt.format("an")))
# second = int(input(prompt.format("a second")))

# if first > second:
#     first, second = second, first

# total = 0
# while first <= second:
#     total += first
#     first += 1

# print("Total = ", total)

# tulisan = "masukan {} :"
# print(tulisan.format("angka"))
# print(tulisan.format("orangnya"))