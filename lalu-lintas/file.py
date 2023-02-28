import time
import os

def lalulintas():
    while True:
        os.system('cls')
        print("BERHENTI !!!")
        for i in range(10, 0, -1):
            mins, secs = divmod(i, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Merah:", timer, end="\r")
            time.sleep(1)

        os.system('cls')
        print("SIAP - SIAP !!!")

        for i in range(3, 0, -1):
            mins, secs = divmod(i, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Kuning:", timer, end="\r")
            time.sleep(1)

        os.system('cls')
        print("JALAN !!!")

        for i in range(10, 0, -1):
            mins, secs = divmod(i, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print("Hijau:", timer, end="\r")
            time.sleep(1)
        break

    os.system('cls')
    print("Program telah selesai!")
    exit()


lalulintas()
