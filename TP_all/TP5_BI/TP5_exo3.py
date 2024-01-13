ch1 = str.lower(input("saisir un mot, une phrase à tester en palindrome : "))

ch2=""

for i in range(len(ch1)):
    if ch1[i].isalpha():
        ch2+=ch1[i]

print(ch2)
i = 0
while (i<len(ch2)/2-1 and ch2[i]==ch2[len(ch2)-1-i]):
    i+=1

if (i < len(ch2)/2-1):
    print("ce n'est pas un palindrome")
else:
    print("c'est un palindrome")


