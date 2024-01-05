flowerbed = [1,0,0,0,1]
n=1


for i in range(0, len(flowerbed)-1):

    if flowerbed[i] == 0 & flowerbed[i - 1] == 0 & flowerbed[i + 1] == 0:
        flowerbed[i+1] = 1
        n = n-1

if n == -1:
    print(True)
else:
    print(False)