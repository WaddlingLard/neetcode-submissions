class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        set_nums: set[int] = set(nums)
        seen_value_table: set[int] = set()
        longest_seq: int = 0

        for num in set_nums:
            if num in seen_value_table:
                continue
            
            parent: int = num - 1
            if parent not in seen_value_table:
                # Start counting
                iteration: int = 1
                next_value: num = num + 1
                seen_value_table.add(num)
                while next_value in set_nums:
                    seen_value_table.add(next_value)
                    iteration += 1
                    next_value += 1
                longest_seq = max(longest_seq, iteration)

        return longest_seq