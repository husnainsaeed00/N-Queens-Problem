class Solution:
    def solveNQueens(self, n):
        def is_safe(board, row, col):
            # Check if a queen can be placed at the given row and col
            for i in range(row):
                if board[i] == col or abs(board[i] - col) == abs(i - row):
                    return False
            return True

        def backtrack(board, row):
            if row == n:
                # All queens are placed, add the solution to the results
                solutions.append(["".join(["Q" if i == col else "." for i in range(n)]) for col in board])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row] = col
                    backtrack(board, row + 1)
                    board[row] = -1

        solutions = []
        board = [-1] * n
        backtrack(board, 0)
        return solutions

# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))
    print(solution.solveNQueens(1))
