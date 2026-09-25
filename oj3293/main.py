"""Big Frame"""
x = []
for i in range(5): #get the texts
    x.append(input().strip())
longest = x[0]
for text in x: #define the logest text
    if len(text) > len(longest):
        longest = text
for i in range(5):
    if not len(longest) - len(x[i]):
        SPACE = 0
    else:
        SPACE = len(longest) - len(x[i])
    if not i:
        print("*" * (len(longest) + 4))
        print(f"* {x[i]}{" "*SPACE} *")
    elif i == 4:
        print(f"* {x[i]}{" "*SPACE} *")
        print("*" * (len(longest) + 4))
    else:
        print(f"* {x[i]}{" "*SPACE} *")
