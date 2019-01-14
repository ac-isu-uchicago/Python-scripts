import re

s = "my number is 123"

match = re.search(r'\d\d\d', s)
match



match.group()

s = "tim email is tim@somehost.com"
match = re.search(r'[\w.-]+@[\w.-]+', s)

# the above regular expression will match a email address

if match:
    print(match.group())
else:
    print("match not found")

import re
s = "tim email is tim@somehost.com"
match = re.search('([\w.-]+)@([\w.-]+)', s)
if match:
    print(match.group()) ## tim@somehost.com (the whole match)
    print(match.group(1)) ## tim (the username, group 1)
    print(match.group(2)) ## somehost (the host, group 2)

s = "Tim's phone numbers are 12345-41521 and 78963-85214"
match = re.findall(r'\d{5}', s)

if match:
    print(match)

s = "Tim's phone numbers are 12345-41521 and 78963-85214"
match = re.findall(r'(\d{5})-(\d{5})', s)
print(match)

for i in match:
    print()
    print(i)
    print("First group", i[0])
    print("Second group", i[1])

s = "python tuts"
match = re.match(r'py', s)
if match:
    print(match.group())

import re
s = "python tuts"
match = re.search(r'^py', s)
if match:
    print(match.group())
