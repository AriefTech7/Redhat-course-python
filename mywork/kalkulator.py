def math():
    riwayat = []

    mulai = True

    while mulai:
        try:
            nmr_1 = int(input("nomor pertama: "))
            operator = input("operator ('+', '-', '*', '/'): ")
            nmr_2 = int(input("nomor kedua: "))

            txt = "hasil = {} "
            hasil_riwayat = "Riwayat Kalkulator:\n{}"

            if operator == "+":
                hasil = nmr_1 + nmr_2
                print(txt.format(hasil))
            elif operator == "-":
                hasil = nmr_1 - nmr_2
                print(txt.format(hasil))
            elif operator == "*":
                hasil = nmr_1 * nmr_2
                print(txt.format(hasil))
            elif operator == "/":
                hasil = nmr_1 / nmr_2
                print(txt.format(hasil))
            else:
                print("your input not valid")
            operato_math = f"{nmr_1} {operator} {nmr_2} = {hasil}"
            riwayat.append(operato_math)
        except ZeroDivisionError:
            print("Error: tidak bisa dibagi dengan nol")


        lanjut = input("hitung lagi y/n: ").lower()
        if lanjut == "n":
            break
    print("\nRiwayat Perhitungan:")
    for each in riwayat:
        print(each)

