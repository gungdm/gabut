"""Buatlah	notasi pengurutan	nilai	dari	array	B	dengan	ketentuan	sebagai	berikut:
Jika	elemen	pertama	bernilai	genap,	maka	setiap	elemen	pada	array	dikalikan	dengan	2	dan	
array	diurutkan	secara	ascending Contoh:	[12,	15,	20,	50,	100]	→	[24,	30,	40,	100,	1000]	
Jika	elemen	pertama	bernilai	ganjil,	maka	setiap	elemen	pada	array	dikalikan	dengan	3	program	
diurutkan	secara	descending Contoh:	[15,	12,	20,	50,	100]	→	[300,	150,	60,	45,	36]"""

#import file sorting.py atau kalau mau report tulis ulang fungsi ascending dan descending di bawah sini
    
test =	[31,24,	61,	12,	13,	20,	27,	22,	20,21,	30,	40,	41,	42,	40,	24] 

def studiCase(arr):
    if test[0] % 2 == 0:
        hasil = [nilai*2 for nilai in ascending(test)]
    
    elif test[0] % 2 == 1:
        hasil = [nilai*3 for nilai in descending(test)]
    
    return hasil

print(studiCase(test))
