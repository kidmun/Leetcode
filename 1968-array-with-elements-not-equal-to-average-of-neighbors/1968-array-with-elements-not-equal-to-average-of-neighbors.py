class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        i = 1
        
        while i < len(nums)-1:
            sum = nums[i-1] + nums[i+1]
            if sum % 2 == 0 and nums[i] == sum // 2:

                nums[i], nums[i+1] = nums[i+1], nums[i]
                if i > 1:
                    i -= 1
            else:
                i += 1

        return nums