class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=0
        ans=[]
        n=len(nums)
        for i in range (n-1):
            for j in range (i+1,n):
                if nums[i]+nums[j] == target:
                    ans.append(i)
                    ans.append(j)
        return ans
