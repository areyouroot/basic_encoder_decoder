import math


def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m


def toString(a):
  l=[]
  m=""
  for i in a:
    b=0
    c=0
    k=int(math.log10(i))+1

    for j in range(k):
      b=((i%10)*(2**j))   
      i=i//10
      c=c+b
    l.append(c)
  for x in l:
    m=m+chr(x)
  return m

word = input("enter the word to be encrypted")
key = input("enter the key")
cmd = input("e - ecryption d - for decryption")


print("''Hello world'' in binary is ") 
print(toBinary("Hello world 123 !@#"))

print(" \n ''[1001000, 1100101, 1101100, 1101100, 1101111,]'' in string is ")
print(toString(toBinary("Hello world 123 !@#")))
