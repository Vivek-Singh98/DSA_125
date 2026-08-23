class Solution:
    def plusOne(self, digits):
        num =0
        for i in digits:
            num = num*10 + i
        num = num +1

        result = [int(i) for i in str(num)]

        return result    