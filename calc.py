print("number")
a = int(input())
print("power")
b = int(input())
print("divided by")
d = int(input())

c = a

for i in range(0, int(b)-1):
    c *= a
print(c%d)