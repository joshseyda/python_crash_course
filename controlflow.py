# if elif else !!! the classic conditional

grade=75
if(grade > 89):
  print("A")
elif(grade > 79):
  print("B")
elif(grade> 70):
  print("C")
else:
  print("try harder!!!!")

# Loops, While and For, machines for automation
# while is until a condition is true
# for is for when you know how long you need to loop for

# While
while(grade<100):
  grade+=5
  if(grade > 89):
    print("A")
  elif(grade > 79):
   print("B")
  elif(grade> 70):
    print("C")
  else:
   print("try harder!!!!")


# take user input with input, convert user input from string to integer...
num = int(input('Enter the value of n= '))
if(num<=0):
    print("Enter a positive number please!")
else:
  sum=0
  while(num>0):
    sum+=num
    num-=1

print(sum)

#  for loop....99 beers

for quant in range(99, 0, -1):
  if(quant > 1):
    print(quant, "bottles of kvass on the wall", quant, "bottles of kvass,")
    if(quant > 2):
      suffix=str(quant)+ " bottles of kvass on the wall"
    else:
      suffix= "1 bottle of kvass on the wall"
  elif(quant == 1):
    print("1 bottle of kvass on the wall, 1 bottle of kvass")
    suffix="no more kvass on the wall"
  print("take one down, pass it around", suffix)
  print("---")

  