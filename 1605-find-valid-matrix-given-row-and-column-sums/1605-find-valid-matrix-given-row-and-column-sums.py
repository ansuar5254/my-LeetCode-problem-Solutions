class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        row,col = len(rowSum),len(colSum)
        res = [[0]*col for _ in range(row)]
        for r in range(row):
            res[r][0] = rowSum[r]

        for c in range(col):
            col_sum = 0
            for r in range(row):
                col_sum += res[r][c]

            r = 0
            while col_sum > colSum[c]:
                diff = col_sum - colSum[c]
                shift = min(diff,res[r][c])
                res[r][c] -= shift
                res[r][c+1] += shift
                col_sum -= shift
                r += 1

        return res


