class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        hasZero = False
        numOfZeros = 0
        for num in nums[1:]:
            if num != 0:
                product *= num
            else:
                hasZero = True
                numOfZeros += 1
        
        res = []
        for num in nums:
            if hasZero:
                if numOfZeros == 1:
                    if num == 0:
                        res.append(product)
                    else:
                        res.append(0)
                else:
                    return [0 for n in nums]
            else:
                res.append(product//num)
        
        return res

        