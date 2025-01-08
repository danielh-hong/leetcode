'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints 
of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1
 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
# Best solution, didn't write this, don't completely completely get it tbh...:
# (Also O(n)):
def maxAreaBest(height):
    """
    :type height: List[int]
    :rtype: int
    """
    i=0
    j=len(height)-1
    maxH=max(height)
    max_area=0
    while i<j:
        if max_area>maxH*(j-i): # works as a way to early dip out because maxH is the max height so maxH*(j-1) must be the max possible val
              print("Max area: ", max_area, "MaxH * (j-1)", maxH*(j-1))
              break
        if height[i]<height[j]:
            area=height[i]*(j-i)
            i+=1
        else:
            area=height[j]*(j-i)
            j-=1
        if max_area<area:
            max_area=area
    return max_area

maxAreaBest([1,3,2,5,25,24,5])

print()

maxAreaBest([1,8,6,2,5,4,8,3,7])

# difficult case: [1,3,2,5,25,24,5]
# Better solution just using two pointers:

def maxArea(height):
    l = 0
    r = len(height) - 1
    m = -1

    while l < r:
        m = max(m, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else: # if they're equal then that HAS to be the max value it can take in so move both
            l += 1
            r -= 1
    return m

# My attempt at solution. Descent but doesn't work.
# Wrong idea. 
# Should just work with the current pointer instead of looking ahead.
class Solution(object):
    def maxAreaBad(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # seems like you ignore all the things between the two pillars

        l = 0
        r = len(height) - 1
        m = r * min(height[l], height[r])
        while l < r:
            print('l ', l)
            print('r ', r)
            m = max(m, (r - l) * (min(height[l], height[r])))
            # if next pillar on the inside smaller, skip this value with the pointer
            # if both inside are smaller, move both in (dont check)
            # if one inside is s, one inside is b, move pointer to big, small stays
            # if both inside are bigger, move to the one that creates bigger result

            if height[l+1] <= height[l] and height[r-1] <= height[r]:
                l += 1
                r -= 1
            elif height[l+1] <= height[l] and height[r-1] > height[r]:
                r -= 1
            elif height[l+1] > height[l] and height[r-1] <= height[r]:
                l += 1
            else: # both inside are bigger, then move to the one that gives big area
                r_a = (r - 1 - l) * min(height[l], height[r-1])
                l_a = (r - l - 1) * min(height[l+1], height[r])
                if r_a >= l_a:
                    r -= 1
                if r_a < l_a:
                    l += 1
                '''

                if height[l] < height[r]:
                    l += 1
                elif height[l] > height[r]:
                    r -= 1
                elif height[l+1] < height[r-1]: # if they are equal check the inside values
                    l += 1
                elif height[l+1] >= height[r-1]:
                    r -= 1
                '''

        return m