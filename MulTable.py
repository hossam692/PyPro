req_num = float (input('Enter Number To Get Multiplication Table: '))

def mul_table(req_num):
	for n in range(0,11):
		print('{0} x {1} = {2}'.format(req_num, n, req_num*n))

mul_table(req_num)
