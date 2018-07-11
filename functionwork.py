# Functions > aka an organized, reuseable set of instructions, implemented to perform related actions

def add(a, b):
  result = a + b
  return result

num1 = 45
num2 = 49
print(add(num1,num2))


def fibo(n):
  a=0
  b=1
  for x in range(n):
    c=a
    a=b
    b=c+b
    print(a, "\n")
  return b
num=int(input("Enter the value of n: "))
print(fibo(num))