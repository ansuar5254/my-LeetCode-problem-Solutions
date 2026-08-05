class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        count = 0
        for val in s:
            n = int(val)
            if n != 0 and num % n == 0:
                count += 1
        return count
