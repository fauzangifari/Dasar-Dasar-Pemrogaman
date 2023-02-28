import os
import datetime
import time
from prettytable import prettytable

mulai = time.time()

user_data = [{"nama": "fauzan", "pin": 14022, "saldo": 50000, "role": "vip"},
             {"nama": "yanto", "pin": 1212, "saldo": 50000, "role": "reguler"}]

list_musik_vip = [{"judul": "Anything You Want", "penyanyi": "Reality Club", "harga": 14000},
                  {"judul": "Evaluasi", "penyanyi": "Hindia", "harga": 11000},
                  {"judul": "Circle", "penyanyi": "Post Malone", "harga": 12000},
                  {"judul": "Tujuh Belas", "penyanyi": "Tulus", "harga": 15000},
                  {"judul": "Usik", "penyanyi": "Feby Putri", "harga": 20000},
                  {"judul": "Fall In Love Alone",
                      "penyanyi": "Stacey Ryan", "harga": 10000},
                  {"judul": "Runtuh",
                      "penyanyi": "Feby Putri ft Fiersa Bersari", "harga": 9000},
                  {"judul": "Kau Adalah", "penyanyi": "Tulus", "harga": 5000}, ]

list_musik_regular = [{"judul": "Anything You Want", "penyanyi": "Reality Club", "harga": 14000},
                      {"judul": "Evaluasi", "penyanyi": "Hindia", "harga": 11000},
                      {"judul": "Circle", "penyanyi": "Post Malone", "harga": 12000},
                      {"judul": "Tujuh Belas", "penyanyi": "Tulus", "harga": 15000},
                      {"judul": "Usik", "penyanyi": "Feby Putri", "harga": 20000}]

voucher = [{"nama": "Kupon Merdeka", "kode": "VOCER1", "potongan": 3000, "use": 1, "expired": mulai + 60, "status": "aktif"},
           {"nama": "Kupon 11.11", "kode": "VOCER2",
               "potongan": 2000, "use": 1, "expired": mulai + 240, "status": "aktif"},
           {"nama": "Kupon Natal", "kode": "VOCER3", "potongan": 1000, "use": 1, "expired": mulai + 120, "status": "aktif"}]

user_session = []

os.system('cls')


def main():

    pilihan = str(input('''
    ========================================
    |          M E N U   P I L I H         |
    ========================================
    |   > 1. Login                         |
    |   > 2. Exit                          |
    ========================================
Masukkan pilihan anda: '''))
    if pilihan == '1':
        os.system('cls')
        login()
    elif pilihan == '2':
        os.system('cls')
        print("Terima kasih")
        os.system('cls')
        time.sleep(1)
        exit()
    else:
        print("Pilihan anda salah")
        main()


def login():
    print("========================================")
    print("                L O G I N               ")
    print("========================================")
    user = str.lower(input("> Masukkan nama anda: "))
    pin = int(input("> Masukkan pin anda: "))
    for i in user_data:
        if i["nama"] == user and i["pin"] == pin:
            user_session.append(i)
            print("========================================")
            print("         Anda berhasil login            ")
            print("========================================")
            time.sleep(1)
            menu()
    print("========================================")
    print("        Nama atau pin anda salah        ")
    print("========================================")
    time.sleep(1)
    os.system('cls')
    login()


def menu():

    pilihan = str(input('''
    ========================================
    |          M E N U   P I L I H         |
    ========================================
    |   > 1. Lihat daftar musik            |
    |   > 2. Beli musik                    |
    |   > 3. Lihat saldo dan voucher       |
    |   > 4. Top up saldo                  |
    |   > 5. Cek Member                    |
    |   > 6. Exit                          |
    ========================================
    Masukkan pilihan anda: '''))
    if pilihan == '1':
        os.system('cls')
        daftar_musik()
        menu()
    elif pilihan == '2':
        os.system('cls')
        daftar_musik()
        beli_musik()
    elif pilihan == '3':
        os.system('cls')
        lihat_saldo()
    elif pilihan == '4':
        os.system('cls')
        top_up()
    elif pilihan == '5':
        os.system('cls')
        role()
    elif pilihan == '6':
        os.system('cls')
        print("Terima kasih")
        time.sleep(1)
        os.system('cls')
        exit()
    else:
        print("Pilihan anda salah")
        menu()


def role():
    if user_session[0]["role"] == "vip":
        print("Member anda:", user_session[0]["role"])
        print("Keuntungan: Mendapatkan potongan setiap pembelian sebesar 15%")
        menu()
    elif user_session[0]["role"] == "reguler":
        print("Member anda:", user_session[0]["role"])
        print("Keuntungan: Anda tidak memiliki keuntungan")
        time.sleep(1)
        print("\nJangan berkecil hati")
        menu()


def daftar_musik():
    print("Daftar musik:")
    if user_session[0]["role"] == "vip":
        t = prettytable.PrettyTable(["No.", "Judul", "Penyanyi", "Harga"])
        nomor = 1
        for i in list_musik_vip:
            t.title = "Daftar Musik VIP"
            t.add_row([nomor, i["judul"], i["penyanyi"], i["harga"]])
            nomor += 1
        print(t)
    else:
        t = prettytable.PrettyTable(["No.", "Judul", "Penyanyi", "Harga"])
        nomor = 1
        for i in list_musik_regular:
            t.title = "Daftar Musik Regular"
            t.add_row([nomor, i["judul"], i["penyanyi"], i["harga"]])
            nomor += 1
        print(t)


def top_up():
    nominal = int(input("Masukkan nominal top up: "))
    user_session[0]["saldo"] += nominal
    print("Top up berhasil, saldo anda sekarang adalah",
          user_session[0]["saldo"])
    for i in user_data:
        if i["nama"] == user_session[0]["nama"]:
            i["saldo"] = user_session[0]["saldo"]
    menu()


def beli_musik():
    global pilihan1
    pilihan1 = int(input("Masukkan nomor musik yang ingin anda beli: "))
    punya_voucher = input("Apakah anda punya voucher? (y/n): ")
    input_voucher = ""
    if punya_voucher == "y":
        input_voucher = input("Masukkan kode voucher anda: ")
    if user_session[0]["role"] == "vip":
        if pilihan1 > len(list_musik_vip):
            print("Nomor musik yang anda masukkan salah")
            daftar_musik()
        elif punya_voucher == "y" and input_voucher not in [i["kode"] for i in voucher]:
            print("Kode voucher yang anda masukkan salah")
            daftar_musik()
        elif punya_voucher == "y" and voucher[[i["kode"] for i in voucher].index(input_voucher)]["use"] == 0:
            print("Kode voucher yang anda masukkan tidak ada")
            time.sleep(1)
            os.system('cls')
            daftar_musik()
            beli_musik()
        else:
            harga_musik = list_musik_vip[pilihan1 - 1]["harga"]
            for i in voucher:
                if i["kode"] == input_voucher:
                    harga_musik -= i["potongan"]
                    i["use"] -= 1
                    i["status"] = "expired"

            user_session[0]["saldo"] -= harga_musik * 15 / 100
            print("Anda mendapatkan potongan harga 15% dari member vip")
            if user_session[0]["saldo"] >= list_musik_vip[pilihan1 - 1]["harga"]:
                print("Anda berhasil membeli",
                      list_musik_vip[pilihan1 - 1]["judul"])
                print("Sisa saldo anda adalah", user_session[0]["saldo"])
                for i in user_data:
                    if i["nama"] == user_session[0]["nama"]:
                        i["saldo"] = user_session[0]["saldo"]
                cetakStruk = str.lower(
                    input("Apakah anda ingin mencetak struk? (y/n): "))
                if cetakStruk == "y":
                    print("Struk berhasil dicetak")
                    time.sleep(2)
                    os.system('cls')
                    strukVip()
                elif cetakStruk == "n":
                    print("Terima kasih telah berbelanja, semoga harimu menyenangkan")
                    time.sleep(2)
                    os.system('cls')
                    menu()
                menu()
            else:
                print("Saldo anda tidak cukup")
                time.sleep(1)
                print("Mohon top up terlebih dahulu")
                time.sleep(1)
                os.system('cls')
                menu()
    else:
        if pilihan1 > len(list_musik_regular):
            print("Nomor musik yang anda masukkan salah")
            daftar_musik()
        elif punya_voucher == "y" and input_voucher not in [i["kode"] for i in voucher]:
            print("Kode voucher yang anda masukkan salah")
            daftar_musik()
        elif punya_voucher == "y" and voucher[[i["kode"] for i in voucher].index(input_voucher)]["use"] == 0:
            print("Kode voucher yang anda masukkan sudah digunakan")
            beli_musik()
        else:
            harga_musik = list_musik_regular[pilihan1 - 1]["harga"]
            for i in voucher:
                if i["kode"] == input_voucher:
                    harga_musik -= i["potongan"]
                    i["use"] -= 1
                    i["status"] = "expired"

            user_session[0]["saldo"] -= harga_musik
            if user_session[0]["saldo"] >= list_musik_regular[pilihan1 - 1]["harga"]:
                print("Anda berhasil membeli",
                      list_musik_regular[pilihan1 - 1]["judul"])
                print("Sisa saldo anda adalah", user_session[0]["saldo"])
                for i in user_data:
                    if i["nama"] == user_session[0]["nama"]:
                        i["saldo"] = user_session[0]["saldo"]
                cetakStruk = str.lower(
                    input("Apakah anda ingin mencetak struk? (y/n): "))
                if cetakStruk == "y":
                    print("Struk berhasil dicetak")
                    time.sleep(2)
                    os.system('cls')
                    strukReguler()
                elif cetakStruk == "n":
                    print("Terima kasih telah berbelanja, semoga harimu menyenangkan")
                    time.sleep(2)
                    os.system('cls')
                    menu()
                menu()
            else:
                print("Saldo anda tidak cukup")
                time.sleep(1)
                print("Mohon top up terlebih dahulu")
                time.sleep(1)
                os.system('cls')
                menu()


def lihat_saldo():
    print("Saldo anda adalah", user_session[0]["saldo"])

    while True:
        for x in voucher:
            if time.time() >= x["expired"]:
                x["use"] = 0
                x["status"] = "expired"
        pocer = prettytable.PrettyTable(
            ["No.", "nama", "Kode", "Potongan", "Tersedia", "Status"])
        nomor = 1
        for i in voucher:
            pocer.title = "Daftar Voucher"
            pocer.add_row([nomor, i["nama"], i["kode"],
                           i["potongan"], i["use"], i["status"]])
            nomor += 1
        print(pocer)
        menu()


def strukVip():
    print("=======================================")
    print("            Struk Pembelian            ")
    print("=======================================")
    print("> Nama       : ", user_session[0]["nama"])
    print("> Tanggal    : ", datetime.datetime.now())
    print("> Judul      : ", list_musik_vip[pilihan1 - 1]["judul"])
    print("> Penyanyi   : ", list_musik_vip[pilihan1 - 1]["penyanyi"])
    print("> Harga      : Rp. ", list_musik_vip[pilihan1 - 1]["harga"])
    print("=======================================")
    print("> Sisa saldo : Rp. ", user_session[0]["saldo"])
    print("=======================================")
    print("Terima kasih menjadi member kami!")
    print("Terima kasih telah berbelanja, semoga harimu menyenangkan")


def strukReguler():
    print("=======================================")
    print("            Struk Pembelian            ")
    print("=======================================")
    print("> Nama       : ", user_session[0]["nama"])
    print("> Tanggal    : ", datetime.datetime.now())
    print("> Judul      : ", list_musik_regular[pilihan1 - 1]["judul"])
    print("> Penyanyi   : ", list_musik_regular[pilihan1 - 1]["penyanyi"])
    print("> Harga      : Rp. ", list_musik_regular[pilihan1 - 1]["harga"])
    print("=======================================")
    print("> Sisa saldo : Rp. ", user_session[0]["saldo"])
    print("=======================================")
    print("Terima kasih menjadi member kami!")
    print("Terima kasih telah berbelanja, semoga harimu menyenangkan")


main()
