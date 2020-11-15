import sys

def reduce_prod(nums):
    product = 1
    for num in nums:
        product *= num
    return product
    
def max_horizontal(grid):
    maximum = 0
    for y in range(len(grid)):
        prod = reduce_prod(grid[y][:4])
        maximum = max(maximum, prod)
        
        for x in range(len(grid[y]) - 4):
            if grid[y][x] != 0:
                prod //= grid[y][x]
        
            if grid[y][x + 4] != 0:
                prod *= grid[y][x + 4]
                
            maximum = max(maximum, prod)
            
    return maximum
    
def transpose(matrix):
    result = [[None] * 20 for i in range(20)]
    for y in range(20):
        for x in range(20):
            result[y][x] = matrix[x][y]
            
    return result
    
def rot45(matrix):
    """Rotates a matrix 45 degrees clockwise"""
    
    result = []
    counter = 0
    n = len(matrix)
    
    while counter < 2 * n - 1:
        l = []
        
        for y in range(n):
            for x in range(n):
                if x + y == counter:
                    l.append(matrix[y][x])
                
        l.reverse()
        result.append(l)
        counter += 1
        
    return result

def rot90(matrix):
    """Rotates a matrix 90 degrees counter-clockwise"""
    
    n = len(matrix)
    return [[matrix[x][n - 1 - y] for x in range(n)] for y in range(n)]

grid = [input().strip().split(' ') for row in range(20)]
grid = [[int(num) for num in row] for row in grid]

horizontal = max_horizontal(grid)
vertical = max_horizontal(transpose(grid))
top_right_diagonal = max_horizontal([row for row in rot45(grid) if len(row) > 4])
bottom_right_diagonal = max_horizontal([row for row in rot45(rot90(grid)) if len(row) > 4])

print (max(horizontal, vertical, top_right_diagonal, bottom_right_diagonal))
