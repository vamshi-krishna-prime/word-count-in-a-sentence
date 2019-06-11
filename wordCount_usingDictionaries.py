str = "it appears that the the appears the most in the sentence"
list = str.split(" ")
dict = {}
for word in list:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

print(f"string = '{str}'")
for key, value in dict.items():
    print(f"The word '{key}' appeared '{value}' times in the above sentence")
