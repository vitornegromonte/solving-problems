class Solution:
    def romanToInt(self, s: str) -> int:
      romanDict = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
      romanEspecialCases = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900 }
      count = 0
      
      for i in range(len(s)):
        for instance in romanEspecialCases:
          if instance in s:
            count += romanEspecialCases[instance]
            s = s.replace(instance, '')

      for x in s:
        count += romanDict[x]
    
      return count
