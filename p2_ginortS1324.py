# Your task is to sort the string s in the following manner:
# 1.All sorted lowercase letters are ahead of uppercase letters.
# 2.All sorted uppercase letters are ahead of digits.
# 3.All sorted odd digits are ahead of sorted even digits.

s="Sorting1234"
lower=''
upper=''
evendigits=''
odddigits=''
for i in s:
    if i.isdigit():
        if int(i)%2==0:
            evendigits+=i
        else:
            odddigits+=i
    else:
        if i.isupper():
            upper+=i
        else:
            lower+=i
print("".join(sorted(lower)+sorted(upper)+sorted(odddigits)+sorted(evendigits)))