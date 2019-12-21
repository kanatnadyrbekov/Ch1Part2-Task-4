Hour1 = int(input("Hour:"))
Minute1 = int(input("Minute:"))
Second1 = int(input("Second:"))
Hour2 = int(input("Hour2:"))
Minute2 = int(input("Minute2:"))
Second2 = int(input("Second2:"))

result = (((Hour1 - Hour2)*3600) + ((Minute1 - Minute2) * 60) + (Second1 - Second2))
print(abs(result))