import re

StringA = "My 2 favorite numbers are 19 and 42."

# [0-9]:Match any digit; same as [0123456789]
# +:Matches 1 or more occurrence of preceding expression.
result1 = re.findall('[0-9]+', StringA)
print (result1)

# Print only the first instance of a number
print (result1[0])

# \S: Matches nonwhitespace.
# *:Matches 0 or more occurrences of preceding expression.
# [ ]: Matches any single character in brackets.
result2 = re.findall('\S*[a]\S*',StringA)
print (result2)


