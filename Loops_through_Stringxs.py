s = "welcome to python"

s.isalnum()
# False

"welcome".isalpha()
# True

"2012".isdigit()
#True

"first Number".isidentifier()
#False

s.islower()
#True

"WELCOME".isupper()
#True

" \t".isspace()
#True

s = "welcome to python"
s.endswith("thon")
#True

s.startswith("good")
#False

print(s.find("come"))
print(s.find("come"))
print(s.find("become"))
print(s.rfind("o"))
print(s.count("o \n"))

s = "string in python"
s1 = s.capitalize()
print(s1)

s2 = s.title()
print(s2)

s = "This is Test"
s3 = s.lower()
print(s3)

s4 = s.upper()
print(s4)

s5 = s.swapcase()
print(s5)

s6 = s.replace("Is" , "Was")
print(s6)




