def gaji() :
    
    from texttable import Texttable
    
    table = Texttable ()
    jawab = "y"
    no = 0
    nama = []
    jabatan = []
    gaji = []
    

    while (jawab == 'y'):
        nama.append(input("\n masukkan nama : "))
        jab = input("\n jabatan : ")
        jabatan.append(jab)

        if (jab == 'admin'):
            (jabatan == 'admin')
            gaji.append(7000000)
            jawab = input("\n tambah lagi? y/t ")
            no+=1
            
        elif (jab == 'guru'):
            (jabatan == 'guru')
            gaji.append(10000000)
            jawab = input("\n tambah lagi? y/t ")
            no+=1

        elif (jab == 'ojek'):
            (jabatan == 'ojek')
            gaji.append(4000000)
            jawab = input("\n tambah lagi? y/t ")
            no+=1

        else:
            print("tidak di gaji")
            from main import login

    for i in range (no):
            
        table.add_rows([['No','Nama','Jabatan','Gaji'],[i+1,nama[i],jabatan[i],gaji[i]]])


    print (table.draw())

