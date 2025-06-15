class Hewan:
    def suara(self):
        pass

class Burung(Hewan):
    def suara(self):
        return "Cuit cuit!"

class Singa(Hewan):
    def suara(self):
        return "rooaar"
class Kucing(Hewan):
    def suara(self):
        return "meowww~"

class Ular(Hewan):
    def suara(self):
        return "bisssssssstttttuuuussssssssssst"


burung = Burung()
singa = Singa()#tanda kurung berfungsi untuk mewarisi program dari class Hewan
kucing = Kucing()
ular = Ular()

print(f"singa mengaumm {singa.suara()}")
print(f"suara burung dipagi hari {burung.suara()}")
print(f"ular berdesis diantara pepohonan {ular.suara()}")
print(f"kucing menggeliat dikasur {kucing.suara()}")