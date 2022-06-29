class Solution:
    rule = {'type' : 0, 'color' : 1, 'name' : 2}
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(1 for item in items if item[self.rule[ruleKey]] == ruleValue)