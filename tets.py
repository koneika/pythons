a = float(input())
print("with commision? Y or N")
d = input()
if d == 'y' or d == 'Y':
	a = a - (0.5/3.33)
	b = float(input())
	c = float(input())

	print(((a/b)/(a/c)*a))
else:
	b = float(input())
	c = float(input())

	print(((a/b)/(a/c)*a))