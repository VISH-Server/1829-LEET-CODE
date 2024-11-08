from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Calculate the maximum possible value with maximumBit bits (all bits set to 1)
        max_val = (1 << maximumBit) - 1
        
        # Calculate the initial total XOR of all elements in nums
        totalXOR = 0
        for num in nums:
            totalXOR ^= num
        
        # Prepare the answer array
        answer = []
        
        # Process each query in reverse order by removing the last element each time
        for num in reversed(nums):
            # Maximize the XOR with totalXOR and max_val
            answer.append(totalXOR ^ max_val)
            # Remove the last element's contribution from totalXOR
            totalXOR ^= num
        
        return answer
