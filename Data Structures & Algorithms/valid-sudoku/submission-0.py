class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        board_value_locations: dict[int, tuple[int, int]] = defaultdict(list)
        board_section_state: dict[tuple[int, int], set[int]] = defaultdict(set)
        # queue: list[int] = []

        # Need to:
        # Parse and store the board
        # Validate each existing tile with its pieces around it
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if item.isdigit():

                    value: int = int(item)

                    # Save into the board state
                    board_value_locations[value].append((i, j))

                    # Save into quadrant check
                    section: tuple[int, int] = int(i / 3), int(j / 3)
                    prev_size: int = len(board_section_state[section])
                    board_section_state[section].add(value)

                    # No change occured, already existing
                    if prev_size == len(board_section_state[section]):
                        return False

        # Use a set to detect if any items are on the same row / col
        for value, coordinate_list in board_value_locations.items():
            row_set: set = set()
            col_set: set = set()
            for coordinate in coordinate_list:
                row_coord, col_coord = coordinate

                row_set_prev_size: int = len(row_set)
                col_set_prev_size: int = len(col_set)

                row_set.add(row_coord)
                col_set.add(col_coord)
                
                # There is one that already exists on that row / col
                if row_set_prev_size == len(row_set) or col_set_prev_size == len(col_set):
                    return False

        return True

