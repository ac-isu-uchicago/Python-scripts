#<= 	smaller than or equal to
#< 	smaller than
#> 	greater than
#>= 	greater than or equal to
#== 	equal to
#!= 	not equal to

print(3 == 4)

print(12 > 3)
print(12 == 12)
#True

i = 10

if i % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


today = "holiday"
bank_balance = 25000
if today == "holiday":
   if bank_balance > 20000:
      print("Go for shopping")
   else:
      print("Watch TV")
else:
   print("normal working day")