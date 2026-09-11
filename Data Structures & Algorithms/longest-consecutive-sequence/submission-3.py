class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # lets try out path compression! :D

        con_seqs: list[set[int]] = []
        seen_values_table: dict[int, int] = {}

        for num in nums:
            parent: int = num - 1
            cons_index: int
            if parent in seen_values_table:
                parent_value: int = seen_values_table[parent]
                seen_values_table[num] = parent_value
                con_seqs[parent_value] = con_seqs[parent_value].union([num])
                cons_index = parent_value
            else:
                seq: set[int] = set([num])
                con_seqs.append(seq)
                seen_values_table[num] = len(con_seqs) - 1
                cons_index = len(con_seqs) - 1

            next_num: int = num + 1
            if next_num in seen_values_table:
                # Apply path compression
                compress_path_set: set[int] = con_seqs[seen_values_table[next_num]]
                con_seqs[cons_index] = con_seqs[cons_index].union(compress_path_set)
                for element in compress_path_set:
                    seen_values_table[element] = seen_values_table[num]

        return max([len(x) for x in con_seqs]) if con_seqs else 0
            