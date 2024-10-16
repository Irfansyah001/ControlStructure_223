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