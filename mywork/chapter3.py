#exercise 3.1

# first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]

# name = []

# for index, day in enumerate(first):
#     name.append(f"{day}{second[index]}")

# print(name)

#exercise 3.2
# prompt = "Enter a number (or the word 'end' to quit) "
# collect_data = []
# while True:
#     data = input(prompt)
#     if data != "end":
#         collect_data.append(int(data))
#     elif data == "end":
#         break
#     #Remainder of while loop goes here
#
# print(collect_data)
# print(f"this is a sum number {sum(collect_data)}")

#exercise 3.3
# a = "-"
# a *= 50
# text = "enter number (or word 'end' to quit): "
# verifikasi = "Are you sure to add number y/n:"
# collect_data_set = set()
# collet_data_tuple = []
# while True:
#     print(a)
#     data = input(text.lower())
#     if data != "end":
#         print(a)
#         ver = input(verifikasi.lower())
#         if ver == "y":
#             collect_data_set.add(data)
#         elif ver == "n":
#             collet_data_tuple.append(data)
#     elif data == "end":
#         break
#     else:
#         print("Error: your not valid")
# print(a)
# print(f"this is type data set {collect_data_set}")
# print(f"this is not type data set {collet_data_tuple}")

#exercise 3.4
# txt = "enter a unique words( or word 'end' to quit this program): "
#
# #type data set
# one_line = set()
#
# #looping
# while True:
#     # lower = mengkonversi ke char kecil
#     data = input(txt).lower()
#     if data != "end":
#         # menambahkan data dari input ke set
#         one_line.add(data)
#     elif data == "end":
#         break
#
#
# for word in one_line:
#     print(word)
#
# print(f"{len(one_line)} words in all")

#exercise 3.5
# number = {
#     0:"zero",
#     1:"one",
#     2:"two",
#     3:"three",
#     4:"four",
#     5:"five",
#     6:"six",
#     7:"seven",
#     8:"eight",
#     9:"nine"
# }
#
# user = input("enter number range 0-9( or the word 'end' to quit): ")
#
# for number_user in user:
#     print(number[int(number_user)], end=" ")

#exercise 3.6

#dict kosong
# collect_dict = {}
# while True:
#     user = input("Enter a some text (or just the word 'end' to quit): ")
#
#     if user == "end":
#         break
#
# #spilt = mengubah string menjadi list
#     # word_list = user.split()
#     # for word_raw in word_list:
#     #     collect_dict[word_raw] = collect_dict.get(word_raw, 0) + 1
#     collect_dict[user] = collect_dict.get(user, 1) + 1
#
# # key_list =list(collect_dict.keys())
# print(collect_dict)
# print()
# print("Words and count sorted by Words (the key)")
# for word in collect_dict.keys():
#     print(word, collect_dict[word])
#
# print("\nWords and Word count sorted by Word Count (the value)")
#
# for word in sorted(collect_dict.keys()):
#     print(word, collect_dict.get(word))