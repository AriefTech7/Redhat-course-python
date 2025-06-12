def jumlah_and_rata(angka):
    jumlahnya = 0
    for i in angka:
        jumlahnya += i
    rata = jumlahnya / len(angka)
    return (f"penjumlahan {jumlahnya} and rata-rata {rata}")


# print(f"ini adalah rata dan penjumlahan dari 9, 8, 7 = jumlah {jumlah_and_rata(9,8,7)}")
# nomor = (9,8,7) # jika kamu menggunakan variabel tuple disaat kamu menggunakan *args yang bertipe tuple akan menjadi error
# print(jumlah_and_rata(nomor))

