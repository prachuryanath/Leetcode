class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_map = {arr2[i] : i for i in range(0,len(arr2))}
        return sorted(arr1, key=lambda a: arr2_map.get(a, 1000 + a))