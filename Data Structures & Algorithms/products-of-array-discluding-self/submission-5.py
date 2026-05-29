class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        pre.append(1)

        prod = nums[0]
        for num in nums[1:]:
            pre.append(prod)
            prod *= num

        

        suf = []
        suf.append(1)
        r_nums = list(reversed((nums)))

        prod = r_nums[0]
        for r_num in r_nums[1:]:
            suf.append(prod)
            prod *= r_num
        r_suf = list(reversed(suf))
        
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * r_suf[i])
        
        return res




        # [1, 1, 2, 8]
        # [48, 24, 6, 1]
        # [48, 24, 12, 8]

                
        