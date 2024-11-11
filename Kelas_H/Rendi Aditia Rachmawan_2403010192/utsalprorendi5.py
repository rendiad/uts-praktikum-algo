# Meminta input kata, indeks awal, dan indeks akhir dari pengguna
kata = input("Masukkan kata: ")
indeks_awal = int(input("Masukkan indeks awal: "))
indeks_akhir = int(input("Masukkan indeks akhir: "))

# Mengambil substring dari indeks_awal hingga indeks_akhir (indeks_akhir tidak termasuk)
substring = kata[indeks_awal:indeks_akhir]

# Menampilkan hasil substring
print(f"Substring: {substring}")

