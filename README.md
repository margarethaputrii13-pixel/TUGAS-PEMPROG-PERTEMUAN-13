# TUGAS-PEMPROG-PERTEMUAN-13
Nama = margaretha futri irwan   
Kelas = TI25.C1.      
Nim = 312510337

I. Tujuan Praktikum.   
	1.	Memahami penggunaan try-except dalam menangani kesalahan (exception) pada program Python.        
	2.	Menerapkan penanganan kesalahan input dan operasi aritmatika.
	3.	Membuat program yang tetap berjalan meskipun terjadi error.

⸻

II. Dasar Teori

Exception handling adalah mekanisme dalam Python untuk menangani kesalahan saat program dijalankan (runtime error). Dengan menggunakan try-except, program dapat menangkap dan menangani error tertentu seperti ValueError, ZeroDivisionError, dan TypeError tanpa menghentikan eksekusi program secara keseluruhan.

Struktur dasar exception handling:
try:
    # kode yang berpotensi error
except JenisError:

V. Hasil dan Pembahasan

A. Latihan 1 – Kalkulator Aman

try:
    a = float(input("Masukkan angka pertama: "))
    b = float(input("Masukkan angka kedua: "))
    op = input("Masukkan operator (+, -, *, /): ")

    if op == "+":
        hasil = a + b
    elif op == "-":
        hasil = a - b
    elif op == "*":
        hasil = a * b
    elif op == "/":
        try:
            hasil = a / b
        except ZeroDivisionError:
            print("Error: Tidak bisa membagi dengan nol")
            exit()
    else:
        raise Exception("Error: Operator tidak valid")

    print("Hasil:", hasil)

except ValueError:
    print("Error: Input harus berupa angka")
except Exception as e:
    print(e)

Pembahasan:
Program ini menggunakan try-except untuk menangani kesalahan input dan operasi pembagian. Jika pengguna memasukkan data yang tidak valid, program akan menampilkan pesan error yang sesuai tanpa berhenti secara paksa.

B. Latihan 2 – Validasi Daftar nilai

nilai = [80, 90, 'A', 70, 100, 'B']

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

	•	List nilai berisi angka dan string ('A', 'B')
	•	try-except digunakan di dalam loop untuk:
	•	Menangani TypeError saat data bukan angka
	•	Melewati data tidak valid tanpa menghentikan program
	•	Rata-rata dihitung hanya dari data nu
