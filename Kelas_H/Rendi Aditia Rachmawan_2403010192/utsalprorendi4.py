# Meminta input kalimat dari pengguna
kalimat = input("Masukkan kalimat: ")

# Mendefinisikan huruf vokal
vokal = "aeiouAEIOU"

# Menghitung jumlah huruf vokal
jumlah_vokal = sum(1 for huruf in kalimat if huruf in vokal)

# Menampilkan jumlah huruf vokal
print(f"Jumlah huruf vokal: {jumlah_vokal}")
