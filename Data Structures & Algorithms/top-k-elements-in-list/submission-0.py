class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency_table: dict[int, int] = defaultdict(int)

        for num in nums:
            frequency_table[num] += 1

        values_sorted: list[tuple(int, int)] = [(freq, element) for element, freq in frequency_table.items()]
        
        values_sorted.sort(reverse=True)

        return [values_sorted[i][1] for i in range(k)]
