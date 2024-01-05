candies = [12,1,12]
extraCandies = 10

largest_candy = max(candies)

new_candies = [x+extraCandies for x in candies]
print(new_candies)
answer_candies = [False] * len(candies)
for i in range(len(new_candies)):
    if new_candies[i] >= largest_candy:
        answer_candies[i] = True

print(answer_candies)