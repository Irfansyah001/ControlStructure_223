'''Write the codes for the following tasks! Then Show it to the teacher or the assistants to get the grades!

When showing the codes, the teacher or the assistants will ask you some questions to see how much you learn
from the materials.'''

'''1. Write a PYTHON program to evaluate the student performance

    If % is >=90 then Excellent performance

    If % is >=80 then  Very Good performance

    If % is >=70 then Good performance

    If % is >=60 then average performance'''
nilai = int(input('Masukan nilai = '))
if nilai >= 90:
    print('Excellent performance')
elif nilai >= 80:
    print('Very Good performance')
elif nilai >= 70:
    print('Good performance')
else:
    print('average performance')

'''2. Write a PYTHON program to find largest of three numbers!'''
nomor1 = input('Masukan nomor pertama = ')
nomor2 = input('Masukan nomor kedua = ')
nomor3 = input('Masukan nomor ketiga = ')

terbesar = max(nomor1, nomor2, nomor3)
print(f'nomor terbesar yaitu: {terbesar}')

'''3. Write a PYTHON program to print Fibonacci series up to n!'''
nomor_untuk_Fibonaci = int(input("Masukan nomor untuk Fibonaci: "))

a, b = 0, 1
print(a)
while b <= nomor_untuk_Fibonaci:
    print(b)
    a, b = b, a + b

'''4. Write a PYTHON program to print odd numbers up to n!'''
nomor_untuk_menampilkan_ganjil = int(input("Masukkan rentang nomor untuk menyering angka ganjil saja: "))

for nomor in range(1, nomor_untuk_menampilkan_ganjil + 1):
    if nomor % 2 == 1: 
        print(nomor)

'''5. Write a PYTHON program to produce following design

    1

    2 2

    3 3 3

    4 4 4 4 

    5 5 5 5 5

    If user enters n value as 5'''

nomor_untuk_setengah_piramid = int(input("masukan nomor untuk membuat setengah piramid: "))

for i in range(1, nomor_untuk_setengah_piramid + 1):
    for j in range(i):
        print(i, end=' ')
    print()