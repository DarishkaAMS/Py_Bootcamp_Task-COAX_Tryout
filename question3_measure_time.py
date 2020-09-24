''' Tryout Task:
Given the array candies and the integer extraCandies, 
where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among 
the kids such that he or she can have the greatest number of candies 
among them. 
Notice that multiple kids can have the greatest number of candies'''

import time

def benchmark(func):
    def wrapper(x, y):
        start = time.time()
        func(x, y)
        end = time.time()
        delta = end - start
        print('The function execution time is {} sec.'.format(delta))

    return wrapper

s = "string"

@benchmark
def kidsWithCandies(candies, extraCandies):
    max_candy = max(candies)
    answer = []
    for kid in candies:
        answer.append(kid + extraCandies >= max_candy)
    return answer

kidsWithCandies([2,3,5,1,3], 3)
 