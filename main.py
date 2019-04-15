from program.penilaian import penilaian
from program.gaji import gaji
from program.kalkulator import kalkulator
from program.pembayaran import pembayaran


def menu() :
    
    print("-----  MENU UTAMA  ----")
    print("\n 1.PENILAIAN MAHASISWA ")
    print("\n 2.GAJI KARYAWAN ")
    print("\n 3.PEMBAYARAN MAHASISWA ")
    print("\n 4.PROGRAM KALKULATOR SEDERHANA ")
    print("\n 5.EXIT")
    pilihan = input("\nMasukkan Pilihan ( 1 \ 2 \ 3 \ 4 \ 5) ? ")
    if pilihan == '1' :
        penilaian()
    elif pilihan == '2' :
        gaji()
    elif pilihan == '3' :
        pembayaran()
    elif pilihan == '4' :
        kalkulator ()
    elif pilihan == '5' :
        print("TERIMA KASIH")
    else :
        print("\nPILIHAN TIDAK DITEMUKAN!!")
    tambahan()
    
   

def tambahan() :
    
    tanya = input("\t\nKembali ke MENU UTAMA : ")
    if tanya == "y" :
        menu()
    elif tanya == "t" :
        print("-----------")
    else :
        print("salah input")
        exit

print("Silahkan Anda Login")       
nama = "iid"
kunci = "1234"
lagi = 'y'
a = 0
while lagi == 'y' :
    username = input("Masukkan Username Anda : ")
    import getpass
    password = getpass.getpass()
    if(username == nama and password == kunci) :
        print("Anda Telah Login")
        break
       
    elif (username == nama or password == kunci) :
        print("username atau password anda salah")
    else :
        print("Password Salah")
    a=a+1
    if a==3 :
        print("sudah 3x input")
        break
        
    print()
    lagi = input("Input kembali, y / t?  ")
    print()
        
menu()

     
