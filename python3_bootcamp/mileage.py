# 1.60934
print("How many kilometers did you run today?")
kms = input()
miles = float(kms)/1.60934
# round(thing to round, how many decimal points)
distance = round(miles, 2)
print(f"Ok, you ran {distance} miles")
