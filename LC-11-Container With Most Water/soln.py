class Solution:
    def maxArea(self, height: List[int]) -> int:
        first = 0
        last = len(height)-1
        max_area = 0

        while first<last:
            area = (last - first)*min(height[first],height[last])
            max_area = max(area,max_area)

            if height[first]<height[last]:
                first+=1
            else:
                last-=1
        return max_area
            
        
