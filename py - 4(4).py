def replace(str1,str2):
    if str2 in str1:
        c=str1.replace(str2,'')
    print(c)
str1=input("enter string 1:")
str2=input("enter string 2:")
replace(str1,str2)
