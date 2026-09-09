class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # Zip up the two lists for ease of access
        zipped: list[tuple[int, int]] = [(p, s) for p, s in zip(position, speed)]
        stack: list[float] = []

        # Sort the list (use the built-in for now)
        zipped.sort(reverse=True)

        for position, speed in zipped:
            stack.append((target - position) / speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)