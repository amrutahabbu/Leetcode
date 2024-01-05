from re import findall

s="leetcode"

s1 =""

vowels = findall('[aeiouAEIOU]', s)
print(vowels)

for i in range(len(s)):

    if s[i].lower() in "aeiouAEIOU":
        currentVowel = s[i]
        newVowel=vowels.pop()
        s1+=newVowel
    else:
        s1+= s[i]


print(s1)