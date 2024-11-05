
'''
[3,2,1]
[1,7,6]
[2,7,7]


'''



grid = [[3,2,1],[1,7,6],[2,7,7]]
class Solution:
    def equalpairs(self, grid) -> int:
        rowcounts = {}
        count = 0
        for row in grid:
            rowcounts[tuple(row)] += 1
        for  column in zip(*grid):
            count+= rowcounts[column]
            print(rowcounts)
        return count 
    print(equalpairs(grid))

