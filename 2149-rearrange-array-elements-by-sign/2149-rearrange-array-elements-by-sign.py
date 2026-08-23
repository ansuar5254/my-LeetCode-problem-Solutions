class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        i = 0
        for num in nums:
            if num > 0:
                ans[i] = num
                i += 2

        i = 1

        for num in nums:
            if num < 0:
                ans[i] = num
                i += 2

        return ans

        