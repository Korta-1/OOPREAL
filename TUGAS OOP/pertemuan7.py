class Karyawan:
    def __init__(self, nama,):
        self.nama = nama
    
    def bekerja(self):
        print(f"{self.nama} sedang melaksanakan tugasnya")

class Manager(Karyawan):
    def bekerja(self):
        print(f"manager {self.nama} sedang memimpin rapat divisi")

class Programmer(Karyawan):
    def bekerja(self):
        print(f"programmer {self.nama} sedang bekerja sembari minnum kopi")

def simulasikan_kerja(karyawan):
    karyawan.bekerja()

manager1 = Manager("Budi")
programmer1 = Programmer("Andi")
simulasikan_kerja(manager1)
simulasikan_kerja(programmer1)
simulasikan_kerja(Karyawan("Siti"))
