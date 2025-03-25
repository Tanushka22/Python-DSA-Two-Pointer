class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers)-1

        if len(numbers)==2:
            return [1,2]

        while first<last:
            total = numbers[first]+numbers[last]
            if total==target:
                return [first+1,last+1]
            elif total>target:
                last-=1
            else:
                first+=1
        
