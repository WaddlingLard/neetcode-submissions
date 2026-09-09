class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 1. Use a default dictionary, no need to check if key is missing now
        character_table: dict[list[tuple[str, int]], list[str]] = defaultdict(list)

        for string in strs:

            chopped_str: list[str] = list(string)

            # 2. Instead of another hashmap, you can represent all characters via their index in a list
            chopped_list: list[int] = [0] * 26 # 26 characters in the alphabet!
            # chopped_table: dict[str, int] = {}
            found_sublist: int = 0

            for character in chopped_str:
                # Convert the character in to ASCII table values
                # Subtracting from the ASCII value of 'a' gets the base point
                # Ex: org('a') - org('a') = 0, which is the first index
                chopped_list[ord(character) - ord("a")] += 1

                # if character not in chopped_table:
                #     chopped_table[character] = 1
                # else:
                #     chopped_table[character] += 1

            # No need to use a frozen set from that hashtable
            # Use a tuple from the iterable list as the key!


            # key = frozenset(chopped_table.items())

            # character_table[key].append(string)
            character_table[tuple(chopped_list)].append(string)

        return [value for value in character_table.values()]