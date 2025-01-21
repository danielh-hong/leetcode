# 605. Can Place Flowers (easy) (complete)
'''
You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means 
empty and 1 means not empty, and an integer n, return true if n new flowers 
can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.'''

'''
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
'''

# my own solution
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # [ 0 1 0 0 1 0 0 1 0 ] <-- can't place anything, since 

        # iterate through the list starting from 1 index,
        # check l + r, decrement n if can place

        if len(flowerbed) == 1 and flowerbed[0] == 1 and n == 1:
            return False
        elif n == 0 or len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0] = 1
            n -= 1

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1

        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1] = 1
            n -= 1
            

        return False if n > 0 else True