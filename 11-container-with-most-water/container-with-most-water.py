class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        max =0
        length = 0
        while(left<right):
            if height[left]<height[right]:
                length = height[left]
            else :
                length = height[right]

            width = right - left 

            area = length * width

            if  area > max:
                max = area

            if height[left]<height[right]:
                left = left +1
            else:
                right = right-1
        return max              





        