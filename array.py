# Membuat list kosong untuk menampung hobi
hobi = []
stop = False
i = 0

# Mengisi data
while (not stop):
    nama=input("Masukan Nama : ")
    golongan=input("Golongan [1/2/3] : ")
    print("Pilihan Status : \nTidak Menikah(T) \nMenikah (M) \nJanda (J) \nDuda (D) ")
    status=input("Status [T/M/J/D] : ")
    hobi_baru = input("Inputkan hobi yang ke-{}:".format(i))
    hobi.append(hobi_baru)
 # Increment i
    i += 1
    tanya = input("Mau isi lagi? (y/t): ")
    if (tanya == "t"):
        stop = True
# Cetak Semua Hobi
print("=" * 10)
print("Kamu memiliki {} hobi".format(len(hobi)))
for hb in hobi:
 print("- {}".format(hb))