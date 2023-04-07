# print("formate of email is ...@gmail.com")
# j,k,l,a,b,c,d,e,f,g,h,p,q=0,0,0,0,0,0,0,0,0,0,0,0,0
# email=input("enter your email:")                       #p@gmai.com=len 9
# if len(email)>=9:                                      # 987654321=index in -ve
#     if email[0].isalpha():
#         for i in email:
#          if i==i.isspace():
#             k=1
#          elif i.isalpha():
#              if i==i.upper():
#                  j=1
#          elif i.isdigit():
#             continue
#          elif i=="_" or i=="." or i=="@":
#             continue
#          else:
#             l=1
#         if j==1 or k==1 or l==1:
#             print(" special chercter and uppercase is not allowed in email except '_'")
#         else:
#             for i in email:
#               if i=="m" and email[-1]=='m':
#                     a=1
#               elif i=="o" and email[-2]=='o':
#                   b=1
#               elif i=="c" and email[-3]=='c':
#                   c=1
#               elif i=="." and email[-4]=='.':
#                   d=1
#               elif i=="l" and email[-5]=='l':
#                   e=1
#               elif i=="i" and email[-6]=='i':
#                   f=1
#               elif i=="a" and email[-7]=='a':
#                   g=1
#               elif i=="g" and email[-9]=="g":
#                   h=1
#               elif i=="@" and email[-10]=='@':
#                   p=1
#               else:
#                   q=1
#             if a==1 and b==1 and c==1 and d==1 and e==1 and f==1 and g==1 and h==1 and p==1 and q==1:
#                 print("email is created correct sucessfully")
#             else:
#                 print("wrong formate check it in instruction")
#     else:
#         print("first letter should be alphabet change it.")
# else:
#  print("the length of gmail is less than 9 so upgread it with correct formate.")       


# #-------------------------------------------------------------------------------------------------------------------------------------------------


# Valid email addresses must follow these rules:
# It must have the username@websitename.extension format type.
# The username can only contain letters, digits, dashes and underscores [a-z],[A-Z],[0-9],[_].
# The website name can only have letters and digits [a-z],[A-Z],[0-9].
# The extension can only contain letters [a-z],[A-Z].
# The maximum length of the extension is 3.

# 3
# lara@hackerrank.com
# brian-23@hackerrank.com
# britts_54@hackerrank.com
def fun(email):
    #using try block
    try:
        # splitting the name and url of the email adress
        username, url = email.split('@')
        website, extension = url.split('.')
   # raise error if the email is not valied     
    except ValueError:
        return False
    # we are not replacing the - and _ 
    if username.replace('-', '').replace('_', '').isalnum() is False:
        return False
    # checking if all characters are alphabets and numerics
    elif website.isalnum() is False:
        return False
    # checking if the length is less than 3
    elif len(extension) > 3:
        return False
    else:
        return True
def filter_mail(emails):
    return list(filter(fun, emails))
if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails) #['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

# #----------------------------------------------------------------------------------------------------------------------------------------

import re
for _ in range(int(input())):
    s = input()
    if re.search(r'<[a-zA-Z][\w\-.]+@[a-zA-Z]+\.[a-zA-Z]{1,3}>', s):
        print(s)
