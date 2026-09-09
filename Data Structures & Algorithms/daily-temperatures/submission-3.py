class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[int] = []
        result: list[int] = [0 for i in range(len(temperatures))]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp: tuple[int, int] = stack.pop()
                result[prev_temp[1]] = index - prev_temp[1]
            stack.append((temp, index))

        while stack:
            prev_temp: tuples[int, int] = stack.pop()
            result[prev_temp[1]] = 0

        return result