
class gontor :
    nama_pimpinan = ' '
    universitas = ' '

    @staticmethod
    def jurusan_unggulan():
        print (f"teknik informatika,agro,kedokteran")

    def profile_rektor(self) :
        print (f"prodi {self.nama_pimpinan} adalah rektor {self.universitas} dengan mata kuliah yang unggul")
    @staticmethod
    def gedung_asrama():
        print (f"ada gedung umar, utsamn,abu bakar, dan al fatih")

gontor = gontor()
gontor.nama_pimpinan = "kh.hamid fahmi zarkasyi"
gontor.universitas = "Universitas Islam darussaalam"
gontor.jurusan_unggulan()
gontor.profile_rektor()
gontor.gedung_asrama()
