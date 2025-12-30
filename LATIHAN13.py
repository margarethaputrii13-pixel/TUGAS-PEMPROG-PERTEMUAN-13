print("NAMA  : MARGARETHA FUTRI IRWAN")
print("NIM   : 312510337")
print("KELAS : TI.25.C5")
nilai = [80, 90, 'A', 70, 100, 'C']

total = 0
jumlah = 0
data_tidak_valid = []

for n in nilai:
    try:
        total += n
        jumlah += 1
    except TypeError:
        data_tidak_valid.append(n)

if jumlah > 0:
    rata_rata = total / jumlah
    print("Data nilai        :", nilai)
    print("Data tidak valid  :", data_tidak_valid)
    print("Jumlah data valid :", jumlah)
    print("Total nilai       :", total)
    print("Rata-rata nilai   :", rata_rata)
else:
    print("Tidak ada data nilai yang valid")