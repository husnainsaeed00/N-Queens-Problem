# N-Queens Problem
The N-Queens problem is a classic puzzle in which we need to place N queens on an N x N chessboard such that no two queens can attack each other. In chess, a queen can move horizontally, vertically, and diagonally, making the placement of queens a challenging problem.

## Problem Statement
Given an integer N, the task is to find all distinct solutions to the N-Queens puzzle. Each solution represents a distinct board configuration of the N-queens' placement, where 'Q' and '.' indicate a queen and an empty space, respectively.

### Example
Input
n = 4
Output

[ [".Q..","...Q","Q...","..Q."], ["..Q.","Q...","...Q",".Q.."] ]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

### Solution Approach
To solve the N-Queens problem, we can use a backtracking approach. We will create a recursive function that explores all possible placements of queens on the board, ensuring that no two queens can attack each other. We'll start by placing a queen in the first row and recursively explore all possible placements in the subsequent rows. If a valid solution is found, it will be added to the list of solutions.

Python Code
Here's the Python code implementing the N-Queens problem using the backtracking approach:
```class Solution:
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

#Test cases

if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))```




The solveNQueens function is part of the Solution class, which implements the backtracking algorithm to find all possible solutions to the N-Queens problem.

Now you can use the Solution class to find solutions for different N values by calling the solveNQueens method with the desired N value.
