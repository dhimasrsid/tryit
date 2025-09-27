def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Meminta input dari pengguna
jumlah = int(input("Masukkan jumlah suku deret Fibonacci yang ingin ditampilkan: "))

print("Deret Fibonacci:")
for i in range(jumlah):
    print(fibonacci(i), end=" ")
