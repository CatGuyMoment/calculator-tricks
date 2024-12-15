def fac(n):  
  factorial = 1
  if int(n) >= 1:
    for i in range (1,int(n)+1):
      factorial = factorial * i
  return factorial
def binm(x, y):
    try:
        return fac(x) // fac(y) // fac(x - y)
    except ValueError:
        return 0
def ptal(m):
        return [binm(m, y) for y in range(m + 1)]
        
a = float(input("a = "))
ifax = int(input("a x coeff?"))
b = float(input("b = "))
ifbx = int(input("b x coeff?"))
n = int(input("n = "))

output = ""
output1 = ""
tabel = ptal(n)
print(tabel)
for i in range(n+1):
    print(i)
    if i != 0:
        output = output + " + "
        output1 = output1 + " + "
    output = output + str(tabel[i]*(a**i) * (b**(n-i)))
    if tabel[i] != 1:
      output1 = output1 + str(tabel[i])
      
      #format identity
      if i != 0 or n-i != 0:
        output1 = output1 + "*"
    if i != 0:
      output1 = output1 + "a"
      if i != 1:
        output1 = output1 +"^" + str(i) 
    if (n-i) != 0:
      output1 = output1  + "b"
      if (n-i) != 1:
        output1 = output1 +"^" + str(n-i)

     #format answer   
    if ifax * i != 0:
        output = output + "x^"+str(ifax*i)
    if ifbx * (n-i) != 0:
        output = output + "x^"+str(ifbx * (n-i))
print(output)
print(output1)
