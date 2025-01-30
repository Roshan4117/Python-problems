a = int (input(""))
b = int(input(""))
if a < 0 and b < 0:
    a = a * -1
    b = b * -1
c = a - b

if c < 0:
    c = c * -1
    print("sum",c)
d = a + b

if  d < 0:
    d = d * -1
    print("diffence",d) 
print ("add & sub",{c},{d})
 