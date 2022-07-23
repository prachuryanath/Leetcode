class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        cnt = max(Counter(ranks).values())
        ans = "High Card"
        if(len(set(suits)) == 1): # 5 of the same
            ans = "Flush"
        elif cnt >= 3:
            ans = "Three of a Kind"
        elif cnt == 2:
            ans = "Pair"
        return ans 
        
