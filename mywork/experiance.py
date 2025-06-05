#args
def sum_number(*numbers):
    tota = 0
    print("paramter type", type(numbers), end=" ")
    for number in numbers:
        tota += number
        return tota

a = sum_number(1, 2, 3, 4, 5)
print(a)


#**kwargs
def function(**input):
    for key, value in input.items():
        print(f"type key {type(key)} and type value {type(value)}")
        print(f"{key} = {value}")

function(name= "udin dirgantara", umur= 23, alamat= "pekanbaru")



#karna menggunakan loop sehingga bisa diakses
def function(*input):
    for asci in input:
        print(f"type {type(asci)}")
        print(f"this your input {asci}")

function("udin", 2, "antot")



#ditampilkan dalam bentuk tuple
def function(*input):
    print(f"type {type(input)}")
    print(f"this your input {input}")

function("udin", 2, "antot")