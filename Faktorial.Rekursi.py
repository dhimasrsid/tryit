def faktorial(n):
    if n == 0:
        return 1
    else:
        print(f"faktorial({n}) dipanggil, menunggu faktorial({n-1})...")
        hasil = n * faktorial(n - 1)
        print(f"Hasil faktorial({n}) = {hasil}")
        return hasil

# Contoh pemanggilan fungsi
angka = int(input("Masukkan angka untuk dihitung faktorialnya: "))
hasil = faktorial(angka)
print(f"\nFaktorial dari {angka} adalah {hasil}")
