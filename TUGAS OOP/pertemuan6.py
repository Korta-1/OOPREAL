
class kendaraan:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def info(self):
        print(f"kendaraan ini adalah {self.merk} dengan warna {self.warna}")

class mobil(kendaraan):
    def hazard_lamp(self):
        print(f"mobil dengan merk {self.merk} memiliki hazard lamp")

class motor(kendaraan):
    def hazard_lamp(self):
        print(f"motor dengan merk {self.merk} memiliki hazard lamp")

mobil1 = mobil("Toyota", "Biru")
mobil1.info()
mobil1.hazard_lamp()

motor1 = motor("Honda", "Merah")
motor1.info()
motor1.hazard_lamp()


#ada aja deh