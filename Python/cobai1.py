# Program Penilaian Mahasiswa

nama = input("Nama mahasiswa: ")
tugas = float(input("Nilai tugas: (0-100): "))
uts = float(input("Nilai UTS: (0-100): "))
uas = float(input("Nilai UAS: (0-100): "))
kehadiran = float(input("Nilai kehadiran: (0-100): "))

# Menghitung nilai akhir
nilai_akhir = (tugas * 0.30) + (uts * 0.30 ) + (uas * 40)

# Menentukan nilai huruf (else-elif-else)
if nilai_akhir >= 85:
    huruf = "A"
elif nilai_akhir >= 70:
    huruf = "b" 
elif nilai_akhir >= 60:
    huruf = "c"
elif nilai_akhir >= 50:
    huruf = "d"
else:
    huruf = "e"

# Menentukan status kelulusan (if bersarang)
if huruf =="E":
    Status = " Tidak lulus (nilai kurang)"
else:
    if kehadiran >=75:
        status = "lulus"
    else:
        status ="tidak lulus (kehadiran kurang)"

# Menentukan predikat ( match-case)
match huruf:
    case "A":
        predikat = "sangat baik"
    case "B" :
        predikat = "baik"
    case "C" :
        predikat ="cukup"
    case "D" :
        predikat = "kurang"
    case "E" :
        predikat = "sangat kurang"

# Menampilkan hasil
print("\n==== HASIL PENILAIAN ====")
print("nama         :", nama)
print("tugas        :", tugas)
print("uts          :", uts)   
print("uas          :", uas)
print("kehadiran    :", kehadiran,  "%")
print("--------------------------")    
print("nilai akhir  :", nilai_akhir)
print("nilai huruf  :", huruf)
print("predikat     :", predikat)
print("status       :", status)
