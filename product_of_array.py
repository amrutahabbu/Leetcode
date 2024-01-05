'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 '''
import numpy

nums = [-1,1,0,3,-3]
arraynums = numpy.array(nums)
answer =[]

for i in range(0, len(nums)):

        curr_number = arraynums[i]
        arraynums[i] = 1
        element = (numpy.prod(arraynums))
        arraynums[i] = curr_number
        answer.append(element)

print(answer)
