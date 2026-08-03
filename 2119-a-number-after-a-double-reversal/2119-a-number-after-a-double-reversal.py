class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num == 0:
            return True
        s = str(num)
        if s[-1] == '0':
            return False
        else:
            return True
        
         
        