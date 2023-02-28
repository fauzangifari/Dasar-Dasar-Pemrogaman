import os
import pymongo
import pwinput
import time
import datetime
import random
from prettytable import PrettyTable
from pymongo import MongoClient

# Database MongoDB
cluster = MongoClient('URI Database MongoDb ')

# Database Name
db = cluster['nama database']

# Collection Name
# --> Identitas Collection untuk menyimpan data user dan admin
identitas = db['nama collection']

# --> Produk Collection untuk menyimpan data produk
produk = db['nama collection']


# Fungsi Buat Login admin dan user
def login():
    print('''\n
===================================================
                     L O G I N
===================================================''')
    global penggunaLogin
    uLogin = str.lower(input("Masukkan user anda: "))
    userLogin = uLogin.capitalize()
    passLogin = str(pwinput.pwinput("Masukkan password anda: "))
    result = identitas.find_one({"nama": userLogin})
    penggunaLogin = userLogin

    if result is None:
        print("Username dan Password anda salah")
        time.sleep(2)
        os.system('cls')
        login()

    elif result['nama'] == userLogin and passLogin == result['pass']:
        print("Berhasil Login")
        if result["role"] == "admin":
            os.system('cls')
            menuAdmin()
        elif result["role"] == "user":
            os.system('cls')
            menuUser()
    else:
        print("Username dan Password anda salah")
        time.sleep(2)
        os.system('cls')
        login()


# Fungsi Buat Ketika User ingin membuat akun
def regis():
    print('''\n
===================================================
                R E G I S T R A S I
===================================================''')
    uRegis = str(input("Masukkan ID baru: "))
    userRegis = uRegis.capitalize()
    cekNama = identitas.find_one({"nama": userRegis})
    if cekNama is not None:
        print("Nama telah digunakan. Silahkan coba nama lain!")
        time.sleep(2)
        os.system('cls')
        regis()
    elif uRegis.isspace() == True or uRegis == '':
        print('Silahkan input data yang benar!')
        time.sleep(1)
        os.system('cls')
        regis()
    else:
        passRegis = str(input("Masukkan Password baru: "))
        if passRegis.isspace() == True or passRegis == '':
            print('Password Error')
            time.sleep(1)
            os.system('cls')
            regis()
        else:
            pass
        saldoRegis = float(input("Masukkan Saldo anda: Rp."))
        identitas.insert_one(
            {"nama": userRegis, "pass": passRegis, "saldo": saldoRegis, "role": "user"})
        print('\n--------- DATA TELAH DIKONFIRMASI ---------')
        print('Username :', userRegis)
        print('Password :', passRegis)
        print('Saldo    : Rp.', saldoRegis)
        cekin = input('Tekan [ENTER] jika sesuai dengan anda input')
        if cekin == '':
            print('Berhasil membuat akun\n')
            os.system('cls')
            login()
        else:
            os.system('cls')
            login()


# Fungsi Menu Utama dari User dan Admin, ketika ingin login atau registrasi akun
def menuUtama():
    os.system('cls')
    loginOrRegis = str(input('''
    =================================
    |            Welcome            |
    |        Furniture Store        |
    =================================
    |>>>>> Silahkan pilih opsi <<<<<|
    |                               |
    |   1. Registrasi Akun          |
    |   2. Login Akun               |
    |   3. Keluar                   |
    |                               |
    =================================
Tentukan opsi anda (1/2/3): '''))
    if loginOrRegis == '1':
        os.system('cls')
        regis()
    elif loginOrRegis == '2':
        os.system('cls')
        login()
    elif loginOrRegis == '3':
        selesai()
    else:
        os.system('cls')
        print('''\n
                Data yang dimasukkan salah
    Mohon untuk memasukkan nomor yang tertera saja''')
        menuUtama()


# ==== ADMIN ====
# Fungsi Tampilan menu admin, ketika login menggunakan akun admin
def menuAdmin():
    print("Selamat Datang", penggunaLogin, "!")
    pilihan_admin = str(input('''
    ==================================
    |            M E N U             |
    ==================================
    |-----> Menu yang tersedia <-----|
    |                                |
    |    1. Lihat Produk             |
    |    2. Tambahkan produk         |
    |    3. Hapus produk             |
    |    4. Update produk            |
    |    5. Sign OUt                 |
    |                                |
    ==================================

Tentukan opsi anda (1/2/3/4/5): '''))

    if pilihan_admin == '1':
        os.system('cls')
        tampilanProduk()
        menuAdmin()
    elif pilihan_admin == '2':
        os.system('cls')
        tampilanProduk()
        tambahProduk()
        menuAdmin()
    elif pilihan_admin == '3':
        os.system('cls')
        hapusProduk()
        menuAdmin()
    elif pilihan_admin == '4':
        os.system('cls')
        updateProduk()
        menuAdmin()
    elif pilihan_admin == '5':
        os.system('cls')
        menuUtama()
    else:
        print('Pilihan anda tidak tersedia')
        time.sleep(1)
        os.system('cls')
        menuAdmin()


# Fungsi menanmpilkan produk apa saja yang ada di toko
def tampilanProduk():
    barang = produk.find({})

    tabel_produk = PrettyTable()
    tabel_produk.field_names = ['Nama Produk',
                                'Kategori', 'Harga', 'Stok Barang']
    for x in barang:
        tabel_produk.add_row(
            [x["Nama Produk"], x["Kategori"], x["Harga"], x["Stok Barang"]])
    print(tabel_produk)


# Fungsi menambahkan produk ke toko
def tambahProduk():
    nm = str(input("Masukkan Nama Produk: "))
    namaProduk = nm.capitalize()
    cekNama = produk.find_one({"Nama Produk": namaProduk})
    if cekNama is None:
        kategori = str(input("Masukkan Kategori Produk: "))
        harga = float(input("Masukkan Harga Produk: "))
        stokBarang = int(input("Masukkan Stok Barang: "))
        produk.insert_one({"Nama Produk": namaProduk, "Kategori": kategori,
                          "Harga": harga, "Stok Barang": stokBarang})
        print('Produk telah dimasukkan')
        tampilanProduk()
    elif namaProduk == cekNama["Nama Produk"]:
        print('Barang anda telah tersedia di Tabel')
        time.sleep(2)
        os.system('cls')
        tampilanProduk()
        tambahProduk()
    else:
        print('Gagal menambahkan produk, Silahkan mencoba lagi!')
        time.sleep(2)
        os.system('cls')
        tambahProduk()


# Fungsi menghapus produk yang ada di toko
def hapusProduk():
    barang = produk.find({})
    tabel_produk = PrettyTable()
    tabel_produk.field_names = ['Nama Produk',
                                'Kategori', 'Harga', 'Stok Barang']
    for x in barang:
        tabel_produk.add_row(
            [x["Nama Produk"], x["Kategori"], x["Harga"], x["Stok Barang"]])
    print(tabel_produk)
    hm = str(input("Silahkan pilih nama produk yang ingin dihapus: "))
    hapusBarang = hm.capitalize()
    produk.delete_one({"Nama Produk": hapusBarang})


# Fungsi mengubah data produk jika ada kesalahan saat menambah produk
def updateProduk():
    barang = produk.find({})
    tabel_produk = PrettyTable()
    tabel_produk.field_names = ['Nama Produk',
                                'Kategori', 'Harga', 'Stok Barang']
    for x in barang:
        tabel_produk.add_row(
            [x["Nama Produk"], x["Kategori"], x["Harga"], x["Stok Barang"]])
    print(tabel_produk)
    nf = input("Silahkan pilih nama barang yang ingin di update: ")
    namaFilter = nf.capitalize()
    fltr = {"Nama Produk": namaFilter}
    updateApa = input('''
    -----------------------------
    | Apa yang ingin di update? |
    |---------------------------|
    |     1. Nama Produk        |
    |     2. Kategori           |
    |     3. Harga              |
    |     4. Stok Barang        |
    -----------------------------

Tentukan opsi anda (1/2/3/4): ''')
    if updateApa == "1":
        namaBarang = str(input("Ubah nama produk: "))
        nilaiBaru = {"$set": {'Nama Produk': namaBarang}}
        produk.update_one(fltr, nilaiBaru)
        print('Proses ...')
        time.sleep(1.5)
        print('Berhasil mengupdate Nama Barang!')
        time.sleep(2)
        os.system('cls')

    elif updateApa == "2":
        kategoriBarang = str(input("Masukkan kategori terbaru: "))
        nilaiBaru = {"$set": {'Kategori': kategoriBarang}}
        produk.update_one(fltr, nilaiBaru)
        print('Proses ...')
        time.sleep(1.5)
        print('Berhasil mengupdate Kategori!')
        time.sleep(2)
        os.system('cls')

    elif updateApa == "3":
        hargaBarang = float(input("Masukkan harga terbaru: "))
        nilaiBaru = {"$set": {'Harga': hargaBarang}}
        produk.update_one(fltr, nilaiBaru)
        print('Proses ...')
        time.sleep(1.5)
        print('Berhasil mengupdate Harga!')
        time.sleep(2)
        os.system('cls')

    elif updateApa == "4":
        stokBarang = int(input("Masukkan stok terbaru: "))
        nilaiBaru = {"$set": {'Stok Barang': stokBarang}}
        produk.update_one(fltr, nilaiBaru)
        print('Proses ...')
        time.sleep(1.5)
        print('Berhasil mengupdate Stok Barang!')
        time.sleep(2)
        os.system('cls')

    else:
        print("Pilihan anda tidak tersedia")
        print("Gagal mengupdate. Silahkan mencoba lagi!")
        time.sleep(2)
        os.system('cls')


# Fungsi untuk menutup database dan keluar dari program
def selesai():
    client = pymongo.MongoClient()
    client.close()
    os.system('cls')
    exit()


# ==== USER ====
# Fungsi Tampilan menu user ketika user berhasil login
def menuUser():
    print("Halo", penggunaLogin)
    print("Selamat Berbelanja!")
    pilihan_user = str(input('''
    ==================================
    |            M E N U             |
    ==================================
    |>>>>>> Menu yang tersedia <<<<<<|
    |                                |
    |    1. Lihat Produk             |
    |    2. Cek Saldo                |
    |    3. Tambah Saldo             |
    |    4. Beli Produk              |
    |    5. Sign Out                 |
    |                                |
    ==================================

Tentukan opsi anda (1/2/3/4/5): '''))

    if pilihan_user == '1':
        os.system('cls')
        tampilanProduk()
        menuUser()
    elif pilihan_user == '2':
        os.system('cls')
        lihatSaldo()
    elif pilihan_user == '3':
        os.system('cls')
        tambahSaldo()
        rSaldo = identitas.find_one({"nama": penggunaLogin})
        print("Saldo anda telah ditambahkan. Saldo saat ini : Rp.",
              rSaldo["saldo"])
        menuUser()
    elif pilihan_user == '4':
        os.system('cls')
        beliProduk()
        menuUser()
    elif pilihan_user == '5':
        os.system('cls')
        menuUtama()
    else:
        print('Data yang masukkan salah')
        os.system('cls')
        menuUser()


# Fungsi menambahkan saldo ke user
def tambahSaldo():

    print("Nominal pengisian saldo minimal Rp.10000")
    inputSaldo = int(input("Masukkan nominal :"))
    if inputSaldo >= 10000:
        print("Sedang di Proses ...")
        identitas.update_one({"nama": penggunaLogin}, {
            "$inc": {"saldo": inputSaldo}})
        time.sleep(2)
    elif inputSaldo == str(inputSaldo):
        print("Inputkan Dengan Benar!")
        time.sleep(2)
        os.system('cls')
        tambahSaldo()
    else:
        print("Gagal menambah saldo, minimal 10.000")
        time.sleep(2)
        os.system("cls")
        tambahSaldo()


# Fungsi jika user ingin melihat saldo
def lihatSaldo():
    saldo = identitas.find_one({"nama": penggunaLogin})
    print("Nama Pengguna :", saldo["nama"])
    print("Sisa Saldo    : Rp.", saldo["saldo"])

    balik = input('\nTekan [ENTER] balik ke menu')
    if balik == '':
        os.system('cls')
        menuUser()
    else:
        os.system('cls')
        menuUser()


# Fungsi jika user membeli produk
def beliProduk():
    listBarang = []
    apakahSudah = 0
    jumlahBarang = 0
    hargaTotal = 0
    while apakahSudah == 0:
        barang = produk.find({})
        tabel_produk = PrettyTable()
        tabel_produk.field_names = ['Nama Produk',
                                    'Kategori', 'Harga', 'Stok Barang']
        for x in barang:
            tabel_produk.add_row(
                [x["Nama Produk"], x["Kategori"], x["Harga"], x["Stok Barang"]])
        print(tabel_produk)
        beliBarang = str(
            input('''Silahkan ketik nama barang yang ingin dibeli: '''))
        cekStok = produk.find_one({"Nama Produk": beliBarang.capitalize()})
        if beliBarang.upper() == "N":
            apakahSudah += 1
            break
        elif cekStok is None:
            print('Barang anda tidak tersedia di tabel!')
            time.sleep(2)
            os.system('cls')
            beliProduk()
        elif cekStok["Stok Barang"] > 0:
            cekBarang = produk.find_one(
                {"Nama Produk": beliBarang.capitalize()})
            if beliBarang.capitalize() == cekBarang["Nama Produk"]:
                print(beliBarang.capitalize(),
                      "telah masuk ke keranjang belanja\n")
                listBarang.append(beliBarang.capitalize())

        else:
            print(beliBarang.capitalize(), "telah habis, mohon pilih yang lain")
            time.sleep(2)
            os.system('cls')
            beliProduk()

        nambahBarang = str.upper(
            input("Apakah anda masih ingin menambah barang? (Y/N)"))
        if nambahBarang == "N":
            apakahSudah += 1
        elif nambahBarang == "Y":
            continue
        else:
            break

    for tambah in listBarang:
        pertambahan = produk.find_one({"Nama Produk": tambah})
        hargaTotal += pertambahan["Harga"]
        jumlahBarang += 1

    os.system('cls')
    print("Anda membeli sebanyak", jumlahBarang, "barang")
    print("Barang dengan total belanja adalah Rp.", hargaTotal)

    pembayaran = input('\nTekan [ENTER] lanjut ke pembayaran!\n')
    customer = identitas.find_one({"nama": penggunaLogin})
    if pembayaran == '' and customer["saldo"] >= hargaTotal:
        identitas.update_one({"nama": penggunaLogin}, {
                             "$inc": {'saldo': -hargaTotal}})
        for namaBarang in listBarang:
            fltr = {"Nama Produk": namaBarang}
            nilaiBaru = {"$inc": {'Stok Barang': -1}}
            produk.update_one(fltr, nilaiBaru)

        print("Pembayaran berhasil")
        while True:
            cetakInvoice = str.upper(input("Cetak invoice? (Y/N)"))
            if cetakInvoice == 'Y':
                hargatotal_str = str(hargaTotal)
                waktu = str(datetime.datetime.now())
                nomorInvoice = str(random.randrange(1000, 10000))
                with open('invoice.txt', 'w+') as f:
                    f.truncate(0)
                    f.write("INVOICE #" + nomorInvoice)
                    f.write("\n\nInvoice Date: " + waktu)
                    f.write("\nKepada: " + penggunaLogin)
                    f.write("\n\n> Deskripsi Barang            : ")
                    for deskripsiBarang in listBarang:
                        f.write(deskripsiBarang + ' | ')
                    f.write("\n> Dengan total belanja senilai: Rp." +
                            hargatotal_str)
                    f.write("\n\n> P A I D\n")
                    f.write("\n> Terimakasih telah berbelanja di Toko Kami")
                    f.close()
                print("INVOICE berhasil di cetak")
                print('Terimakasih telah berbelanja!')
                time.sleep(2)
                os.system('cls')
                menuUser()
            if cetakInvoice == 'N':
                print('Terimakasih telah berbelanja!')
                time.sleep(1)
                print('Semoga Hari Mu Menyenangkan!')
                time.sleep(2)
                os.system('cls')
                time.sleep(2)
                menuUser()
            else:
                os.system('cls')
    else:
        produk.update_one({"Nama Produk": listBarang}, {
                          "$inc": {"Stok Barang": + 1}})
        print("Gagal melakukan pembayaran, silahkan membeli lagi")
        time.sleep(2)
        os.system('cls')
        beliProduk()

menuUtama()
