# Parent Class berupa menu
class Menu:
    def __init__(self, nama):
        self.nama = nama
        
    def tampilkan(self):
        print(f"Menu: {self.nama}")
        
    def pesan(self):
        print(f"Memesan: {self.nama}")

# Child Class (Main Course)
class Makanan(Menu):
    def tampilkan(self):
        print(f"Makanan: {self.nama}, Jenis: {self.jenis}")

# Child Class 2 (Beverage)
class Minuman(Menu):
    def tampilkan(self):
        print(f"Minuman: {self.nama}, Ukuran: {self.ukuran}")

# Child Class 3 (Dessert)
class Desert(Menu):
    def tampilkan(self):
        print(f"Desert: {self.nama}, Jenis Desert: {self.jenis_desert}")

# Object Menu
mie_goreng = Makanan("Indomie Goreng")
mie_goreng.jenis = "Main Course"

kwetiaw = Makanan("Kwetiaw")
kwetiaw.jenis = "Main Course"

nasi_rames = Makanan("Nasi Rames")
nasi_rames.jenis = "Main Course"

ovaltine_ice = Minuman("Ovaltine Ice")
ovaltine_ice.ukuran = "Small"

lychee_tea = Minuman("Lychee Tea")
lychee_tea.ukuran = "Medium"

Sakura_Lee = Minuman("Sakura Lee")
Sakura_Lee.ukuran = "Large"

red_velvet = Desert("Red Velvet")
red_velvet.jenis_desert = "Cake"

cheese_cake = Desert("Cheese Cake")
cheese_cake.jenis_desert = "Cake"

mango_sago = Desert("Mango Sago")
mango_sago.jenis_desert = "Beverage"
 
# Call Object
print("                                   ")
print('_______________*Menu*______________')
semua_menu = [
    mie_goreng,
    kwetiaw,
    nasi_rames,
    ovaltine_ice,
    lychee_tea,
    Sakura_Lee,
    red_velvet,
    cheese_cake,
    mango_sago
]

for menu in semua_menu:
    menu.tampilkan()

print("                                  ")
print("__________*List Pesanan*__________")

kwetiaw.pesan()
red_velvet.pesan()
lychee_tea.pesan()