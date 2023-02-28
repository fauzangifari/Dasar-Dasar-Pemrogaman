# User bisa input nilai
# User bisa input operator

def kalkulator():
    '''Fungsi Kalkulator'''

    print("---------Selamat Datang di Kalkulator Sederhana---------")
    nilai1 = float (input('Masukkan nilai 1: '))
    nilai2 = float (input('Masukkan nilai 2: '))
    operator = input('''
Pilih operator matematika yang ingin anda gunakan.

+  Untuk Pertambahan
-  Untuk Pengurangan
*  Untuk Perkalian
/  Untuk Pembagian
%  Untuk Modulo atau Sisa Bagi
** Untuk Pangkat
// Untuk Pembagian Bulat

\nMasukkan operator matematika yang ingin anda gunakan: ''')

    print('==============================================')

    print("Nilai 1:",nilai1)
    print("Nilai 2:",nilai2)
    print("Operator yang anda pilih:",operator)
     
    if operator == '+' :
        print('''Hasil:''',nilai1 + nilai2)
    elif operator == '-':
        print('''Hasil:''',nilai1 - nilai2)
    elif operator == '*':
        print('''Hasil:''',nilai1 * nilai2)
    elif operator == '**':
        print('''Hasil:''',nilai1 ** nilai2)
    elif operator == '/':
        print('''Hasil:''',nilai1 / nilai2)
    elif operator == '%':
        print('Hasil:',nilai1 % nilai2)
    elif operator == '//':
        print ('Hasil:',nilai1 // nilai2)
    else:
        print("Data yang ada masukkan salah!")

    perulangan()
def perulangan():
    '''Fungsi Perulangan'''
    
    halo = str(input('''\nApakah Mau Mengunakan lagi?
Tulis Y untuk Iya
Tulis N untuk Tidak
Jawaban: '''))

    if halo.upper() == 'Y':
        kalkulator()
    elif halo.upper() == 'N':
        print("\nTerimakasih sudah menggunakan kalkulator sederhana.")
    else:
        print('Selesai')
        
kalkulator()
