class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # Start with sorting the nums [negative values -> positive values]
        # Use a set to store the result, return in a list definition
        nums.sort()
        result: set[tuple[int,int,int]] = set()

        # Base condition: if the length of the list is less than 3, return an empty array
        # (solutions do not exist)
        if len(nums) < 3:
            return list(result)

        # A loop will have the middle pointer start from 1 to the 2nd to last element 
        # (buffer room for left and right pointers)
        # Get the left (middle_ptr - 1) and right pointer (middle_ptr + 1) values
        # Calculate the sum inside the while condition (use :=)
        for middle_ptr in range(1, len(nums) - 1):
            left_ptr: int = middle_ptr - 1
            right_ptr: int = middle_ptr + 1
            sum: int
        
            while (left_ptr > -1 and right_ptr < len(nums)):
                sum = nums[left_ptr] + nums[right_ptr]
                # IF the sum === 0, save the result
                # else if sum < 0, iterate the right_ptr
                # else the sum > 0, so iterate the left_ptr
                if sum == -nums[middle_ptr]:
                    result.add((nums[left_ptr], nums[middle_ptr], nums[right_ptr]))
                    left_ptr -= 1                
                elif sum > -nums[middle_ptr]:
                    left_ptr -= 1
                else:
                    right_ptr += 1

        # Return the results from the afformentioned method
        return [[left, middle, right] for left, middle, right in result]
