import math
string='AABCAAADA'
k=math.floor((len(string))/3)
r=[]            #['AAB', 'CAA', 'ADA']

for i in range(0,(len(string)),k):
    r.append(str(string[i:i+k]))

rem1=''
rem2=''
rem3=''
s=[]
v=r[0]        #aab
t=r[1]        #caa
u=r[2]        #ada
    
for i in v:
    if i not in rem1:
        rem1=rem1+i
s.append(rem1)               #ab  
for j in t:
    if j not in rem2:
        rem2=rem2+j
s.append(rem2)               #ca
for k in u:
    if k not in rem3:
        rem3=rem3+k
s.append(rem3)               #ad
          
print(s)      