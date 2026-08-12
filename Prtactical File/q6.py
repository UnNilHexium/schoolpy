vowel,consonant,uppercase,lowercase=0,0,0,0
with open("file.txt","r") as f:
    for i in f:
        for j in i:
            if j.isalpha():
                if j.lower() in ("a","e","i","o","u"):
                    vowel+=1
                else:
                    consonant+=1
            if j.isupper():
                uppercase+=1
            elif j.islower():
                lowercase+=1
print("No. of vowels - ", vowel)
print("No. of consonants", consonant)
print("No. of Uppercase letters", uppercase)
print("No. of Lowecase letters", lowercase)