def anagram(str1, str2):
    if ''.join(sorted(str1.lower())).strip() == ''.join(sorted(str2.lower())).strip():
        print("ANAGRAM")
    else:
       print("NOT ANAGRAM")
str1=input("Enter string 1")
str2=input("Enter string 2")
anagram(str1,str2)

