class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            row_no_p = [int(i) for i in row if i != "."]
            if len(row_no_p) != len(set(row_no_p)):
                return False
        
        for col in [list(r) for r in zip(*board)]:
            col_no_p = [int(i) for i in col if i != "."]
            if len(col_no_p) != len(set(col_no_p)):
                return False

        quadrant_map = defaultdict(list)
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                quadrant_map[(i//3, j//3)].append(num)
        
        for square in quadrant_map.values():
            square_no_p = [int(i) for i in square if i != "."]
            if len(square_no_p) != len(set(square_no_p)):
                return False

        return True