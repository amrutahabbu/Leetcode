
word1 = "eastnorth"
word2 = "westsouth"

resultword = ""

if len(word1) >= len(word2):
    for i in range(len(word1)):
        char1 = word1[i]
        if len(word2) > i:
            char2 = word2[i]
        else:
            char2 = ""
        resultword = resultword + char1 + char2
else:
    for i in range(len(word2)):
        char2 = word2[i]
        if len(word1) > i:
            char1 = word1[i]
        else:
            char1 = ""
        resultword = resultword + char1 + char2

print(resultword)