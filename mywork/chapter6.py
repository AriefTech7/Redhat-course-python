# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def nama(self):
#         print(f"hello my friend {self.name}")
#     def umur(self):
#         return f"saya berumur {self.age}"
#
#
# p1 = Person("arifff", "29")
# p1.nama()
# print(p1.umur())



#exercise 6.1
class Person:
    def __init__(self, name, age, gender):
        self.nama = name
        self.umur = age
        self.kelamin = gender

    def __str__(self):
        return f"{self.nama}:{self.umur}, {self.kelamin}"


# orang = Person("udin satyanto", 19, "menn")
# print(orang)

#exercise 6.2
# class Family(Person):
#     def __init__(self, parent1, parent2, *children):
#         self.ortu1 = parent1
#         self.ortu2 = parent2
#         self.anak = list(children)#attribute bisa diganti menjadi type data lain
#
#     def add(self, kid):
#         self.anak.append(kid)
#
#     def __str__(self):
#         family = str(self.ortu1) + " " + str(self.ortu2)
#         for kid in self.anak:
#             family += "\n\t" + str(kid)
#         return family
#
#
#
# def main():
#     mother = Person("Mom", 45, "F")
#     father = Person("Dad", 45, "M")
#     kid1 = Person("Johnie", 2, "M")
#     kid2 = Person("Janie", 3, "F")
#     myfamily = Family(mother, father, kid1, kid2)
#     kid3 = Person("Paulie", 1, "M")
#     myfamily.add(kid3)
#     print(myfamily)
#
#
# if __name__ == "__main__":
#     main()

#exercise 6.3

# class Banding:
#     def __init__(self, *member):
#         self.anggota = member
#
#     def number_of_anggota(self):
#         return max(0, len(self.anggota))
#
#     def __str__(self):
#         return f"{self.anggota}"
#
#     def __eq__(self, other):
#         if not isinstance(other, Banding):
#             return NotImplemented
#         return self.number_of_anggota()  == other.number_of_anggota()
#
#     def __gt__(self, other):
#         if not isinstance(other, Banding):
#             return NotImplemented
#         return self.number_of_anggota() > other.number_of_anggota()
#
#     def __lt__(self, other):
#         if not isinstance(other, Banding):
#             return NotImplemented
#         return self.number_of_anggota() < other.number_of_anggota()
#
#
# def main1():
#     mama = "andriana"
#     bapak = "andir"
#     anak1 = "jane"
#     anak2 = "jack"
#     anak3 = "jeff"
#     family_udin = Banding(mama, bapak, anak1, anak2)
#     family_abdul = Banding(mama, bapak, anak1, anak3)
#     print(f"family udin {family_udin}")
#
#
#     if family_udin > family_abdul:
#         print("udin have more kids than abdul")
#     elif family_udin == family_abdul:
#         print("families have same # of kids")
#     elif family_udin < family_abdul:
#         print("udin have fewer kids than abdul")
#
#     print(f"family abdul {family_abdul}")
# if __name__ == "__main__":
#     main1()



#exercise 6.4
class Worker:
    def __init__(self, name, salary:float, years:int):
        self.nama = name
        self.gaji = salary
        self.tahun = years

    def pension(self):
        pensiun = self.tahun * (0.1 * self.gaji)
        return f"{pensiun:.3f}"

    def name(self):
        return self.nama

    def __str__(self):
        return f"nama = {self.nama}, gaji = ${self.gaji:.3f}, lama bekerja diperusahaan {self.tahun} tahun dan uang pensiun = ${self.pension()}"

class Manager(Worker):
    def __init__(self, name, salary:float, years):
        super().__init__(name, salary, years)
        self.gaji = salary
        self.tahun = years

    def pension(self):
        pensiun = self.tahun * (0.2 * self.gaji)
        return f"{pensiun:.3f}"


class Executive(Manager):
    def __init__(self, name, salary:float, years):
        super().__init__(name, salary, years)
        self.gaji = salary
        self.tahun = years

    def pension(self):
        pensiun = self.tahun * (0.3 * self.gaji)
        return f"{pensiun:.3f}"


print("gaji pertahun")
worker1 = Worker(name="andi", salary=60, years=5)
print(worker1)
manager = Manager(name="timo",salary=120, years=6)
print(manager)
eksekutif = Executive(name="arif", salary=250, years=9)
print(eksekutif)
