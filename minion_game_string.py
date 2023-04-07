# Game Rules

# Both players are given the same string,S .
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.

# For Example:
# String S = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.




# def minion_game(string):
#     n=string
#     v="aeiouAEIOU"
#     o=0
#     for i in n:
#         o+=1
#     a=[]
#     for i in range(o):
#         for j in range(1,(o-(i-1))):
#             p=(n[i:i+j])
#             a.append(p)
    
#     b=[]
#     c=[]    
#     for k in a:
#         if k[0] not in v:
#             c.append(k)
#         else:
#             b.append(k)
#     d=[]
#     d.append(b)
#     d.append(c)
#     for i in d:
#         if len(d[0])>len(d[1]):
#             pk="Kevin"
#             pk1=len(d[0])
#         elif len(d[0])==len(d[1]):
#             pk="Draw"
#             pk1=None
#         else:
#             pk="Stuart"
#             pk1=len(d[1])
#     return print(pk,pk1)

# if __name__ == '__main__':
#     s = input("enter the string of game")
#     minion_game(s)

# #or

def minion_game(string):
    vowel="AOEUI"
    vowCounter=0
    conCounter=0
    i=0
    while i < len(string):
        
        if  string[i] in vowel :
            vowCounter+=len(string)-i
        else:
            conCounter+=len(string)-i
        i+=1
    
    if vowCounter>conCounter:
        print ("Kevin",vowCounter)
    elif vowCounter<conCounter :
        print ("Stuart",conCounter)
    else :
         print("Draw")
if __name__ == '__main__':
    s = input("enter the string of game")
    minion_game(s)