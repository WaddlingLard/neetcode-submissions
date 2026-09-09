class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table: Dict[int, int] = {}
        result: List[int] = []
        current_index: int = -1
        # stack: list[int] = []

        for index, num in enumerate(nums2):
            table[num] = index

        for num in nums1:
            current_index = table[num]
            for i in range(current_index + 1, len(nums2)):
                if num < nums2[i]:
                    result.append(nums2[i])
                    current_index = -1
                    break

            if current_index != -1:
                result.append(-1)
            
        return result
        