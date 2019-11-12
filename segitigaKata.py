#  ------------------------ Selasa, 12 November 2019 -----------------------------------

# segitigaKata('Purwadhika')
# segitigaKata('Purwadhika Startup and Coding School @BSD')
# segitigaKata('kode')
# segitigaKata('kode python')
# segitigaKata('lintang')

def segitigaKata(kata):
    if len(kata) >= 10:
        kk = 0
        x = kata
        for k in range(int(len(x)/2)):
            hasil = ''
            z = len(x) + 10
            for i in range(z):
                hasil += x[k + i + kk] + ' '          # Solusi ada disini dengan penambahan kk, tapi tidak terjadi??
                if k != i:
                    continue
                # elif k >= 1 and k == i :
                #     kk = kk + k
                    # break
                else:
                    break
            kk += k
            print(hasil)
        hasil = ''
    else:
        print('Mohon maaf, jumlah karakter tidak memenuhi syarat membentuk pola.')

segitigaKata('Purwadhika')
x = 'Purwadhika'
#                       k i
# 0                     0,0
# 1  2                  1,0     1,1
# 3  4  5               2,0,1   2,1,1    2,2,1
# 6  7  8  9            3,0,3   3,1,3    3,2,3   3,3,3
# 10 11 12 13 14        4,0,6   4,1,6    4,2,6   4,3,6   4,4,6
# 15 16 17 18 19 20     5,0,10  5,1,10   5,2,10  5,3,10  5,4,10   5,5,10

# Catata dulu
def eNumber(x):
    for i in range(x, 0, -1):
        number = ''
        for j in range(i, 0, -1):
            number += str(j) + ' '
        print(number)
# eNumber(5)