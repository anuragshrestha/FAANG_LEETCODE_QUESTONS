"""
1219. Path with Maximum Gold
Company: Google
Problem Link: https://leetcode.com/problems/path-with-maximum-gold/description/
"""

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """ 

        
        DIRECTIONS = [(-1, 0), (0, 1), (1,0), (0,-1)]
        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0

        def dfs_backtrack(grid, rows, cols, row, col):
          
            if row < 0 or col < 0 or row == rows or col == cols or \
                    grid[row][col] == 0:
                return 0
            max_gold = 0

          
            original_val = grid[row][col]
            grid[row][col] = 0

         
            for direction in DIRECTIONS:
                r, c = direction
                max_gold = max(max_gold,
                               dfs_backtrack(grid, rows, cols, 
                                             r + row,
                                             c + col))

       
            grid[row][col] = original_val
            return max_gold + original_val

        for row in range(rows):
            for col in range(cols):
                max_gold = max(max_gold, dfs_backtrack(grid, rows, cols, row, 
                                                       col))
        return max_gold