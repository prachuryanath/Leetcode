class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = dict(Counter(ransomNote))
        dict2 = dict(Counter(magazine))
        
        for i in dict1 :
            if not i in dict2 :
                return False
            else:
                if dict1[i] > dict2[i] :
                    return False
        return True