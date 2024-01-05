temperatures = [30,60,90]
answer = [0] * len(temperatures)


count = 0
for i in range(0,len(temperatures)):
    for j in range(i,len(temperatures)):
        temp = 0
        if i==j:
            continue
        if temperatures[i] < temperatures[j]:
            temp = j - i
            answer[i]=temp
            temp = 0
            break

print(answer)
