a = ""
word = input("Enter Word:")
for i in range(0,len(word)):
    if word[i].isalpha():
        a = a + word[i]
if a.lower() == a.lower()[::-1]:
    print("Is palindrome")
else:
    print("Not Palindrome")