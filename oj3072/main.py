"""[LEARNING LOGS] A-E-I-O-U"""

text = input().lower()
vowels = ["a", "e", "i", "o", "u"]
for vowel in vowels:
    count = text.count(vowel)
    if count > 0:
        print(f"{vowel} : {count}")
