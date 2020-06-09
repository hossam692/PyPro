def myfunc(*args):

    mylist = []
    mylist = list(''.join(args))
    for n in range(len(mylist)):
        if n % 2 == 0:
            mylist[n] = mylist[n].upper()
        else:
            mylist[n] = mylist[n].lower()
    mystr = ''.join(mylist)
    return mystr

result = myfunc(input('Enter a word: '))
print(result)