
class Karyawan():
    def __init__(self, nama, golongan, status, gaji_pokok,tunjangan, total_gaji):
        self.nama=nama
        self.golongan=golongan
        self.status=status
        self.gaji=gaji_pokok
        self.tunjangan=tunjangan
        self.total=total_gaji
        

    def menu():
        print("PROGRAM GAJI KARYAWAN")
        print("")
        nama=input("Masukan Nama : ")
        golongan=input("Golongan [1/2/3] : ")
        print("Pilihan Status : \nTidak Menikah(T) \nMenikah (M) \nJanda (J) \nDuda (D) ")
        status=input("Status [T/M/J/D] : ")
        print("")
        if golongan=="1":
            gajipokok=2500000
            if status=="M":
                tunjangan=2500000*10/100
            else:
                tunjangan=2500000*0

        elif golongan=="2":
            gajipokok=3000000
            if status=="M":
                tunjangan=3000000*10/100
            else:
                tunjangan=3000000*0

        elif golongan=="3":
            gajipokok=5000000
            if status=="M":
                tunjangan=5000000*10/100
            else:
                tunjangan=5000000*0
        
        if status=="T":
            sts="Tidak Menikah"
        elif status=="M":
            sts="Menikah"
        elif status=="J":
            sts="Janda"
        elif status=="D":
            sts="Duda"
        else:
            sts("Error!")

        total_gaji= gajipokok+tunjangan
        print("--------GAJI KARYAWAN-----")
        print("Karyawan Yang Bernama : ",nama)
        print("Golongan : ",golongan)
        print("Status : ", sts)
        print("Gaji Pokok : ",gajipokok)
        print("Tunjangan  : ",tunjangan)
        print("Total Gaji : ",total_gaji)

    menu()
