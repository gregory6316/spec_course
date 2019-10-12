from os import R_OK, access
def letters(l):
	dictionary = {}
	for i in l:
		print(i)
		f = open(i,'r',encoding='utf-8')
		for k in f:
			for j in k:
				if j.isalpha():
					if j in dictionary.keys():
						dictionary[j] += 1
					else:
						dictionary[j] = 1
		f.close()
	return dictionary
user_input = input('Введите файлы через запятую: ')
s = user_input.split(',')
flag = 0
for i in s :
	if not(access(i,R_OK)):
		flag += 1
		break
if not flag:
	d = letters(s)
	for i in d:
		print(i,':',d[i])
else:
	print('Один или несколько из файлов не читается(-ются)!')