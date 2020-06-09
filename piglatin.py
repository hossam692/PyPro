def Pig_Latin(inword= 'Word'):
	s = inword.lower()
	slist = list(s)
	vowels = ['a', 'e', 'i', 'o', 'u', 'y']
	if slist[0] in vowels:
		print(s+'ay')
	else:
		print(s[1:]+s[0]+'ay')

Pig_Latin(input('Enter a word: '))