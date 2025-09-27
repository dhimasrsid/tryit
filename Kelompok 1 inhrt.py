#Parent Class 
class kendaraan:
    def __init__(self, company: str, bbm: int, jarak_perliter_: int):
        self.company = company
        self.bbm = bbm
        self.jarak_perliter = jarak_perliter_        
#Child Class 
class Mobil(kendaraan):
    def run(self, jarak_km: int) -> str:
        # Hitung bahan bakar yang dibutuhkan untuk jarak yang diberikan
        bahan_bakar_dibutuhkan = jarak_km / self.jarak_perliter
        
        # Periksa apakah ada cukup bahan bakar
        if bahan_bakar_dibutuhkan <= self.bbm:
            self.bbm -= bahan_bakar_dibutuhkan  # Kurangi jumlah bahan bakar
            return "berhasil dijalankan"
        else:
            return "bahan bakar tidak cukup"
# panggil
if __name__ == "__main__":
    mobil_saya = Mobil("BMW F30", 20, 15)  # 20 liter bahan bakar, 15 km per liter
    print(mobil_saya.run(100))  #"berhasil dijalankan"karena bahan bakar untuk tempuh 100km
    print(mobil_saya.run(200))  #"bahan bakar tidak cukup" akan bisa berjalan namun tdak menempuh 200km
        