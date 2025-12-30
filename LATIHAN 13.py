print("NAMA  : MARGARETHA FUTRI IRWAN")
print("NIM   : 312510337")
print("KELAS : TI.25.C5")
try:
    # Input angka
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    # Input operator
    operator = input("Masukkan operator (+, -, *, /): ")
    # Proses perhitungan
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
        hasil = angka1 - angka2
    elif operator == "*":
        hasil = angka1 * angka2
    elif operator == "/":
        hasil = angka1 / angka2
    else:
        # Operator tidak valid
        raise Exception("Operator tidak valid! Gunakan +, -, *, atau /")

    print("Hasil:", hasil)

except ValueError:
    print("Error: Input harus berupa angka.")

except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol.")

except Exception as e:
    print("Error:", e)