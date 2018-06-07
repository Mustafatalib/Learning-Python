



wrd = input("Plz enter a word: ")
wrd = str(wrd)
rev = wrd[::-1]
print(rev)
if wrd == rev:
    print("Thid word is palindrome")
else:
    print("this word is not a palindrome")
