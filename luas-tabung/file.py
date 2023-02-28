# Program Sederhana Menghitung Luas Tabung

# login dengan pengecekan username dan password secara bersamaan

print('----------Selamat Datang-----------')
print('----Registrasi terlebih dahulu.----\n')

username = input('Registrasi username anda: ')
password = input('Registrasi password anda: ')

print('\n--------DATA TELAH DI KONFIRMASI.--------')
print('Silahkan masukkan data yang telah anda buat')

count = 3

while count >= 0:

    count -= 1
    username1 = input('Masukkan username anda: ')
    password1 = input('Masukkan password anda: ')

    if username == username1 and password == password1:
        print('\nLogin Berhasil')
        count += 1
        break
    elif count == 0:
        break
    else:
        print('\nUsername dan password anda tidak sesuai')
        print('Login Kembali. Tersisa ', count , ' kali lagi.\n')

if count == 0:
    print('\nLogin Gagal.')
    exit()
 
#rumus luas tabung 2 π r (r + t)
#r = jari-jari atau setengah nilai dari diameter sisi lingkaran bagian alas/tutup
#t = tinggi antara sisi lingkaran bagian alas dengan tutup

print("\n------Program Sederhana menghitung Luas Tabung------")

def program():
    '''Fungsi Program'''
    jari_jari = float(input('\nMasukkan Jari-Jari Lingkaran: '))
    tinggi = float(input('Masukkan Tinggi Lingkaran: '))
    phi = 22 / 7

    hasil = 2 * phi * jari_jari * (jari_jari + tinggi)
    print("Luas Tabung:",hasil)

    perulangan()

def perulangan():
    '''Fungsi Perulangan program'''

    coba_lagi = str(input('''\nCoba lagi?
Tulis Y untuk Iya
Tulis N untuk Tidak
Jawaban:'''))

    if coba_lagi.upper() == 'Y':
        program()
    elif coba_lagi.upper() == 'N':
        print("\nTerimakasih sudah menggunakan Program Sederhana menghitung Luas Tabung.")
    else:
        print('\nSelesai')
program()
