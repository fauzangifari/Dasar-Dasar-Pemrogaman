import os
import time
kamus = [{"keluarga": "Keluarga merupakan satu lingkup lingkungan sosial terkecil yang dimiliki setiap individu\n"},
         {"manusia": "Manusia (Homo sapiens) adalah spesies primata yang berasal dan tinggal di bumi dengan populasi terbesar, persebaran yang paling luas, dan dicirikan dengan kemampuannya untuk berjalan di atas dua kaki, serta otak yang kompleks yang mampu membuat peralatan, budaya, dan bahasa yang rumit.\n"},
         {"kucing": "Kucing adalah spesies mamalia dari famili Felidae (keluarga kucing). Kucing adalah hewan peliharaan yang paling banyak dijumpai di dunia. Kucing dapat hidup di berbagai habitat, baik di darat maupun di air. Kucing dapat hidup di berbagai habitat, baik di darat maupun di air.\n"},
         {"mahasiswa": "Mahasiswa adalah seorang yang sedang menempuh pendidikan di perguruan tinggi atau universitas.\n"},
         {"kampus": "Kampus adalah istilah yang digunakan untuk menyebut sebuah kawasan yang berisi bangunan-bangunan pendidikan tinggi, seperti perguruan tinggi dan universitas.\n"},
         {"kota": "Kota adalah sebuah wilayah yang terdiri dari beberapa kecamatan yang memiliki pemerintahan sendiri. Kota adalah sebuah wilayah yang terdiri dari beberapa kecamatan yang memiliki pemerintahan sendiri.\n"},
         {"kabupaten": "Kabupaten adalah sebuah wilayah yang terdiri dari beberapa kecamatan yang memiliki pemerintahan sendiri. Kabupaten adalah sebuah wilayah yang terdiri dari beberapa kecamatan yang memiliki pemerintahan sendiri.\n"},
         {"provinsi": "Provinsi adalah sebuah wilayah yang terdiri dari beberapa kabupaten/kota yang memiliki pemerintahan sendiri. Provinsi adalah sebuah wilayah yang terdiri dari beberapa kabupaten/kota yang memiliki pemerintahan sendiri.\n"},
         {"indonesia": "Indonesia adalah sebuah negara di Asia Tenggara yang terdiri dari pulau-pulau besar dan pulau-pulau kecil di Samudra Pasifik. Indonesia adalah sebuah negara di Asia Tenggara yang terdiri dari pulau-pulau besar dan pulau-pulau kecil di Samudra Pasifik.\n"}]

os.system('cls')


def main_menu():
    print("====================================")
    print("|               MENU               |")
    print("====================================")
    print("| > 1. Lihat kamus                 |")
    print("| > 2. Cari kata                   |")
    print("| > 3. Keluar                      |")
    print("====================================")
    menu = str(input("Tentukan pilihan anda: "))
    if menu == "1":
        os.system('cls')
        lihat_kamus()
    elif menu == "2":
        os.system('cls')
        cari_kata()
    elif menu == "3":
        os.system('cls')
        exit()
    else:
        print("Menu tidak tersedia")
        time.sleep(1)
        os.system('cls')
        main_menu()


def lihat_kamus():
    os.system('cls')
    for kata in kamus:
        for key in kata:
            print(f"{key}: {kata[key]}")
    main_menu()


def cari_kata():
    kata = str.lower(input("Masukkan kata yang ingin dicari: "))
    for kata_dic in kamus:
        for key in kata_dic:
            if kata == key:
                print(f"{key}: {kata_dic[key]}")
                main_menu()
    print("Kata tidak ditemukan!")
    cari_kata()

main_menu()
