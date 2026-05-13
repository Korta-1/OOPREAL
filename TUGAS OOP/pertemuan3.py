
class Bank:
    nama = ''
    saldo = 0 

    def cek_saldo(self):
        print (f'print dari method cek_saldo')

    def __init__(self, nama= ' ' , saldo=0):
        if saldo < 0:
            print (f'saldo tidak boleh negatif')
        self.nama = nama
        self.saldo = saldo
        print (f'uluul')
    
    def __str__(self):
        return f'ayyo berhasil'
    
    def __eq__ (self, other):
        if self.nama == other.nama and self.saldo == other.saldo:
            return True
    
    def __lt__ (self, other):
        if self.saldo < other.saldo:
            return True
        
bank1 = Bank('Korta',1000000)
bank2 = Bank('Korta',1000000)

print (bank1==bank2)