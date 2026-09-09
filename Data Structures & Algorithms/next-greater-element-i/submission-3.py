class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table: Dict[int, int] = {}
        result: List[int] = []
        stack: list[int] = []

        for num in nums2:
            
            while stack and num > stack[-1]:
                previous = stack.pop()
                table[previous] = num
        
            stack.append(num)

        for num in nums1:
            if num in table:
                result.append(table[num])
            else:
                result.append(-1)

        return result
        