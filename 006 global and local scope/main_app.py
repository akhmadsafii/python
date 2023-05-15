# Global dan Local scope

nama_global = "otong"  # <- ini variabel global

# akses variabel global dalam fungsi
def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# Percabangan
if True:
    print(f"if menampilkan {nama_global}")

## Variable Local Scope

def fungsi2():
    nama_local = "Ucup" # <- variabel lolal scope

fungsi2()
# print(nama_local) # tidak bisa dilakukan bos

# Contoh 1 : Penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")

nama = "Otong"
say_otong()

# Contoh 2: merubah variabel global
