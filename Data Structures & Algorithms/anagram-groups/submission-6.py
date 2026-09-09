class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        character_table: dict[list[tuple[str, int]], list[str]] = {}

        for string in strs:

            chopped_str: list[str] = list(string)
            chopped_table: dict[str, int] = {}
            found_sublist: int = 0

            for character in chopped_str:
                if character not in chopped_table:
                    chopped_table[character] = 1
                else:
                    chopped_table[character] += 1

            key = frozenset(chopped_table.items())

            if key in character_table:
                character_table[key].append(string)
            else:
                character_table[key] = [string]

        return [value for value in character_table.values()]