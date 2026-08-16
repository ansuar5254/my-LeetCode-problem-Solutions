class Solution:
    def sumOfMultiples(self, n: int) -> int:
        divisor = [3,5,7]
        summ = 0
        for i in range(3,n+1):
            for n in divisor:
                if i % n == 0:
                    summ += i
                    break

        return summ


        