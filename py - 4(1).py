count=0
str1=input("enter a string:")
for i in range(len(str1)):
    if(str1[i]=='a'or str1[i]=='e'or str1[i]=='i' or str1[i]=='o'or str1[i]=='u'):
        count+=1
print(count)
