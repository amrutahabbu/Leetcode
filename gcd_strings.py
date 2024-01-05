str1 = "ABABAB"
str2 = "ABAB"
longString = ""
shortString = ""
num1 = len(str1)
num2 = len(str2)
gcd = 1

for i in range(min(num1, num2), 1, -1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
        break


if (str1 + str2) != (str2 + str1):

    # if str1 and str2 has no common factor, then reject
    print(" Nothing")

elif str1 == str2:

    # if str1 and str2 are perfect match, then we find greatest common divisor of strings
    print(str1)

else:
    answer = str1[:gcd]
    print(answer)
