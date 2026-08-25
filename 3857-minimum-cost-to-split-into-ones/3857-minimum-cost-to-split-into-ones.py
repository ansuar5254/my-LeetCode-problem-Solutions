class Solution:
    def minCost(self, n: int) -> int:
        ans = 0
        for i in range(1,n):
            ans +=(n-i)

        return ans
        