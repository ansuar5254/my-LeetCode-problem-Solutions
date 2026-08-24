class Solution:
    def minOperations(self, n: int) -> int:
        m = n//2
        ans = 0
        if n % 2:
            i = 2
            while m:
                ans += i
                i += 2
                m -= 1

        else:
            i = 1
            while m:
                ans += i
                i += 2
                m -= 1

        return ans


        