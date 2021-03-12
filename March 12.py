class Solution:
   def hasAllCodes(self, s: str, k: int) -> bool:
      num = 2**k
      for i in range(num):
         code = str(format(i, f'0{k}b'))
         if code not in s:
            return False
      return True
