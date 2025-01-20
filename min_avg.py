class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        left = 0
        right = len(nums)-1
        min_avg = float('inf')

        while left <= right:
            avg = nums[left]+nums[right]
            avg = avg/2
            min_avg = min(avg,min_avg)
            left+=1
            right-=1

        return min_avg
