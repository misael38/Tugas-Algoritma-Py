import math

# Menentukan luas bangun datar
def hasil_luas(nama_bangun, luas, rumus):
    print(f"\n=== Penghitungan {nama_bangun} ===")
    print(f"Dengan Rumus {rumus}, sehingga didapat:")
    print(f"Luas = {luas} cm^2")
    print("=========================")

# Menentukan keliling bangun datar
def hasil_keliling(nama_bangun, keliling, rumus):
    print(f"\n=== Keliling {nama_bangun} ===")
    print(f"Dengan Rumus {rumus}, sehingga didapat:")
    print(f"Keliling: {keliling} cm")
    print("=========================")
    
# Menentukan volume bangun ruang
def hasil_volume(nama_bangun, volume, rumus):
    print(f"\n=== Keliling {nama_bangun} ===")
    print(f"Dengan Rumus {rumus}, sehingga didapat:")
    print(f"Volume: {volume} cm^3")
    print("=========================")

# Bingkai judul program
print("===========================================")
print("Kelompok 1 Algoritma dan Pemrograman (Math)")
print("===========================================")

print("Anggota Kelompok :")
print("1. Eufrasia Mokili")
print("2. Marvil Lawa")
print("3. Militya Sambali")
print("4. Misael Telleng")
print("5. Rachel Manopo")
print("===========================================")
# Memilih bangun datar
print("Berikut Pilihannya:")
print("1. Luas Bangun Datar")
print("2. Keliling Bangun Datar")
print("3. Volume Bangun Ruang")

pilihan = input("Masukkan nomor pilihan (1-3): ")

# Memasukkan nilai sesuai dengan pilihan
if pilihan == '1':
    print("Silahkan Pilih Nomor Bangun Datar Yang Ingin Dihitung Luasnya")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar Genjang")
    print("6. Trapesium")
    print("7. Belah Ketupat")
    print("8. Layang Layang")

    pilihanl = input("Masukkan nomor pilihan (1-8): ")

    if pilihanl == '1':
        s = float(input("Masukkan panjang sisi persegi: "))
        luas = s * s
        rumus = ("L = s * s")
        hasil_luas("Persegi", luas, rumus)

    elif pilihanl == '2':
        p = float(input("Masukkan Panjang Persegi Panjang: "))
        l = float(input("Masukkan Lebar Persegi Panjang: "))
        luas = p * l
        rumus = ("L = p * l")
        hasil_luas("Persegi Panjang", luas, rumus)

    elif pilihanl == '3':
        a = float(input("Masukkan alas segitiga: "))
        t = float(input("Masukkan tinggi segitiga: "))
        luas = 0.5 * a * t
        rumus = ("L = 1/2 * a * t")
        hasil_luas("Segitiga", luas, rumus)

    elif pilihanl == '4':
        r = float(input("Masukkan jari-jari lingkaran: "))
        luas = math.pi * r * r
        rumus = ("L = pi * r * r")
        hasil_luas("Lingkaran", luas, rumus)

    elif pilihanl == '5':
        a = float(input("Masukkan alas jajar genjang: "))
        t = float(input("Masukkan tinggi jajar genjang: "))
        luas = 0.5 * a * t
        rumus = ("L = 1/2 * a * t")
        hasil_luas("Jajar Genjang", luas, rumus)

    elif pilihanl == '6':
        a = float(input("Masukkan panjang sisi a Trapesium: "))
        b = float(input("Masukkan panjang sisi b Trapesium: "))
        t = float(input("Masukkan tinggi Trapesium: "))
        luas = 0.5 * (a + b) * t
        rumus = ("L = 1/2 * (a + b) * t")
        hasil_luas("Trapesium", luas, rumus)

    elif pilihanl == '7':
        d1 = float(input("Masukkan panjang sisi diagonal pertama belah ketupat: "))
        d2 = float(input("Masukkan panjang sisi diagonal kedua belah ketupat: "))
        luas = 0.5 * d1 * d2
        rumus = ("L = 1/2 * d1 * d2")
        hasil_luas("Belah Ketupat", luas, rumus)

    elif pilihanl == '8':
        d1 = float(input("Masukkan panjang sisi diagonal pertama layang layang: "))
        d2 = float(input("Masukkan panjang sisi diagonal kedua layang layang: "))
        luas = 0.5 * d1 * d2
        rumus = ("L = 1/2 * d1 * d2")
        hasil_luas("Layang Layang", luas, rumus)

elif pilihan == '2':
    print("Silahkan Pilih Nomor Bangun Datar Yang Ingin Dihitung Kelilingnya")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar Genjang")
    print("6. Trapesium")
    print("7. Belah Ketupat")
    print("8. Layang Layang")

    pilihank = input("Masukkan nomor pilihan (1-8): ")

    if pilihank == '1':
        s = float(input("Masukkan Panjang Sisi Persegi: "))
        keliling = 4 * s
        rumus = ("K = 4 * s")
        hasil_keliling("Persegi", keliling, rumus)

    elif pilihank == '2':
        p = float(input("Masukkan Panjang Persegi Panjang: "))
        l = float(input("Masukkan Lebar Persegi Panjang: "))
        keliling = 2 * (p + l)
        rumus = ("K = 2 * (p + l)")
        hasil_keliling("Persegi Panjang", keliling, rumus)

    elif pilihank == '3':
        a = float(input("Masukkan Sisi a Segitiga: "))
        b = float(input("Masukkan Sisi b Segitiga: "))
        c = float(input("Masukkan Sisi c Segitiga: "))
        keliling = a + b + c
        rumus = ("K = a + b + c")
        hasil_keliling("Segitiga", keliling, rumus)

    elif pilihank == '4':
        r = float(input("Masukkan Jari - Jari Lingkaran: "))
        keliling = math.pi * 2 * r
        rumus = ("K = pi * 2 * r")
        hasil_keliling("Lingkaran", keliling, rumus)

    elif pilihank == '5':
        a = float(input("Masukkan Panjang Sisi a Jajar Genjang: "))
        b = float(input("Masukkan Panjang Sisi b Jajar Genjang: "))
        keliling = 2 * (a + b)
        rumus = ("K = 2 * (a + b)")
        hasil_keliling("Jajar Genjang", keliling, rumus)

    elif pilihank == '6':
        a = float(input("Masukkan Panjang Sisi a Trapesium: "))
        b = float(input("Masukkan Panjang Sisi b Trapesium: "))
        c = float(input("Masukkan Panjang Sisi c Trapesium: "))
        d = float(input("Masukkan Panjang Sisi d Trapesium: "))
        keliling = a + b + c + d
        rumus = ("K = a + b + c + d")
        hasil_keliling("Trapesium", keliling, rumus)

    elif pilihank == '7':
        s = float(input("Masukkan Panjang Sisi Belah Ketupat: "))
        keliling = 4 * s
        rumus = ("K = 4 * s")
        hasil_keliling("Belah Ketupat", keliling, rumus)

    elif pilihank == '8':
        a = float(input("Masukkan Panjang Sisi a Layang Layang: "))
        b = float(input("Masukkan Panjang Sisi b Layang Layang: "))
        keliling = 2 * (a + b)
        rumus = ("K = 2 * (a + b)")
        hasil_keliling("Layang Layang ", keliling, rumus)

elif pilihan == '3':
    print("Silahkan Pilih Nomor Bangun Datar Yang Ingin Dihitung Volumenya")
    print("1. Kubus")
    print("2. Balok")
    print("3. Prisma Segitiga")
    print("4. Limas Segitiga")
    print("5. Limas Segiempat")
    print("6. Tabung")
    print("7. Kerucut")
    print("8. Bola")

    
    pilihanv = input("Masukkan Nomor Pilihan (1-8): ")

    if pilihanv == '1':
        s = float(input("Masukkan Panjang Sisi Kubus: "))
        volume = s * s * s
        rumus = ("V = s * s * s")
        hasil_volume("kubus", volume, rumus)

    elif pilihanv == '2':
        p = float(input("Masukkan Panjang Balok: "))
        l = float(input("Masukkan Lebar Balok: "))
        t = float(input("Masukkan Tinggi Balok: "))
        volume = p * l * t
        rumus = ("V = p * l * t")
        hasil_volume("Balok", volume, rumus)

    elif pilihanv == '3':
        a = float(input("Masukkan Alas Prisma Segitiga: "))
        ta = float(input("Masukkan Tinggi Alas Prisma Segitiga: "))
        t = float(input("Masukkan Tinggi Prisma Segitiga: "))
        volume = a * ta * t/3
        rumus = ("V = 1/3 * a * ta * t")
        hasil_volume("Prisma Segitiga", volume, rumus)

    elif pilihanv == '4':
        a = float(input("Masukkan Alas Limas Segitiga: "))
        ta = float(input("Masukkan Tinggi Alas Limas Segitiga: "))
        t = float(input("Masukkan Tinggi Limas Segitiga: "))
        volume = a * ta/2 * t/3
        rumus = ("V = 1/3 * 1/2 * a * ta * t")
        hasil_volume("Limas Segitiga", volume, rumus)

    elif pilihanv == '5':
        s = float(input("Masukkan Alas Limas Segiempat Persegi: "))
        t = float(input("Masukkan Tinggi Limas Segiempat Persegi: "))
        rumus = ("V = s * s * s")
        hasil_volume("Limas Segiempat Persegi", rumus)
       
    elif pilihanv == '6':
        r = float(input("Masukkan Jari Jari Tabung: "))
        t = float(input("Masukkan Tinggi Tabung: "))
        volume = math.pi * r * r * t
        rumus = ("V = pi * r * r * t")
        hasil_volume("Tabung", volume, rumus)

    elif pilihanv == '7':
        r = float(input("Masukkan Jari Jari Kerucut: "))
        t = float(input("Masukkan Tinggi Kerucut: "))
        volume = math.pi * r * r * t/3
        rumus = ("V = 1/3 * pi * r * r * t")
        hasil_volume("Kerucut", volume)

    elif pilihanv == '8':
        r = float(input("Masukkan Jari Jari Bola: "))
        volume = math.pi * 4 * r * r * r/3
        rumus = ("V = 4/3 * pi * r * r * r")
        hasil_volume("Kerucut", volume)

else:
    print("Pilihan Tidak Valid! Silahkan Memilih Nomor (1-3)")
