import coba
import collect

y = collect.collect()
x = coba.jumlah_and_rata(y)
gabung = ", ".join(map(str, y))


print(f"ini adalah hasil dari {gabung} = {x}")


