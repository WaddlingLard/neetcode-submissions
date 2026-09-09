class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left: int = 0
        right: int = len(nums) - 1
        middle: int = int(right - left / 2) + left

        while True:
            if left > right:
                return -1
            elif nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
            middle = int(right - left / 2) + left